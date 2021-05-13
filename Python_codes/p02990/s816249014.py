from operator import mul
from functools import reduce

def main():

    def cmb(n,r):
        r = min(n-r,r)
        if r == 0: return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1,r + 1))
        return over // under

    n, k = map(int, input().split())
    mod = 10**9+7

    # 青をi個に分割する組みわせ
    # i個に分割するにはi-1個区切りが必要
    # 区切りを入れられる場所はk-1
    # k-1Ci-1 
    for i in range(1, k+1):
        #cmb(k-1, i-1))
    # 赤の分割
    # 分け方として0を許すように考えて
    # n-k個 + 端2つをi+1に分割する（n-k+1の選べる場所からi個区切りを選ぶ（青がi個だから））
        #cmb(n-k+2, i)
        if n-k+1 >= i:
            print(cmb(k-1, i-1) * cmb(n-k+1, i) % mod)
        else:
            print(0)

if __name__ == '__main__':
    main()