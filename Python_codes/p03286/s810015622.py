#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list
#from itertools import combinations # (string,3) 3回

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    n = int(input())
    # S_0はNが奇数の時1で、そうでないとき0にする必要があります
    # 基本的にはNを-2で割って、割った余りを答えに追加していくような感じ。
    # N = (-2)q + r
    # としたときに、rが0か1になるようにqを調節するということになります。
    # Nが偶数ならr = 0
    # Nが奇数ならr = 1
    # 単にNを2で割るのと変わらない
    # N % 2 の値は0か-1になるので、 -1 になるならそれに２を足す
    str_ = ""
    while n != 0:
        # N を2で割ったあまりを求める
        r = n % 2
        if r < 0:
            r += 2 # nがマイナスだと、rがマイナスになったりするので2を足す
        n = (n-r)// (-2)
        # - 2で割る
        str_ += str(r)
    #向きが逆なので反転
    str_ = str_[::-1]
    if str_ == '':
        str_ = '0'
    print(str_)



if __name__ == '__main__':
  main()
