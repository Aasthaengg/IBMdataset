import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(1000000)

def main():
    s = readline().rstrip().decode()
    K = int(readline())
    #sに含まれる文字を一文字ずつ抽出する.
    #ここで抽出した文字を組み合わせて辞書順に文字列を構成していく
    l = sorted(list(set(s)))

    #cnd:=構成した文字列を辞書順に格納するリスト
    cnd = []

    #f(sub):=subから構成可能なK文字以下のSの部分文字列を構成する関数

    #計算量について
    #長さNの文字列から作るsubstringのうち長さが5以下のsubstringの数を計算する
    #長さ5のsubstirngは(N-5+1)個
    #長さ4のsubstringは(N-4+1)個
    #同様に長さ1まで考えて、合計すると約5N個となる

    def f(sub):
        cnd.append(sub)
        if len(sub) <= K: 
            #lから選んでsubに一文字追加する
            for i in l:
                nx = sub+i
                #if nx in s:はO(N)
                if nx in s:
                	f(nx)
    #O(N^2K)
    for i in l:
        f(i)
    print(cnd[K-1])
if __name__ == '__main__':
    main()
