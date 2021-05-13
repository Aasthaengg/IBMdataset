import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from bisect import bisect_left 
from operator import itemgetter
def main():
    n, q = map(int, readline().split())
    STX = []
    for _ in range(n):
        s, t, x = map(int, readline().split())
        STX.append((s, t, x))
    D = []
    for _ in range(q):
        d = int(readline())
        D.append(d)

    STX.sort(key=itemgetter(2))

    ans = [-1 for _ in range(q)]
    skipTo = [-1 for _ in range(q)]
    for s, t, x in STX:
        #Dは狭義単調増加列で与えられている
        #s-x<=d<t-xとなるようなDの要素dが格納されている範囲のインデックスを求める
        #以下のようにすれば[left,right]のdがs-x<= d < t-xを満たす
        left = bisect_left(D, s-x)
        right = bisect_left(D, t-x)

        #xが小さいほど早い時刻で歩くのを止めることになる
        #よって、xの昇順に並んでいるので初めて[left, right)の範囲に入ったときだけansを更新するようにしたい
        #skiptoリストを用いて初めてでないときは飛ばすようにする
        while left < right: 
            if skipTo[left] == -1:
                #[left, right)は"このforループ"でansが決まる
                #よってleftが以前ansを決めたインデックスならright未満まではansが決まっているはずなのでrightまでとばす
                #そのためにrightを記録する
                skipTo[left] = right
                ans[left] = x
                left += 1
            else:
                #sikipTo[left]未満はansが決まっているので飛ばす
                left = skipTo[left] 
    for i in ans:
        print(i)
if __name__ == '__main__':
    main()
