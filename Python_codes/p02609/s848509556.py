import sys
read = sys.stdin.read
from collections import defaultdict
def main():
    n = int(input())
    x = list(input())
    # 0除算よけ。
    if n == 1:
        if x[0] == '1':
            print(0)
        else:
            print(1)
        sys.exit()
    # xの10進数換算と１の数カウント。
    x10 = int("".join(x), 2)
    xcount1 = x.count('1')
    # 2**i(mod 1の数)をケースごとに用意する。
    mod2plus = [0] * n
    mod2plus[0] = (1 % (xcount1+1)) # 必ず1になる。xcount1=0はありえない。
    for j1 in range(1, n):
        mod2plus[j1] = (mod2plus[j1 - 1] * 2) % (xcount1+1)
    mod2minus = [0] * n
    if xcount1 > 1:
        mod2minus[0] = 1
        for j1 in range(1, n):
            mod2minus[j1] = (mod2minus[j1 - 1] * 2) % (xcount1-1)
    # x(mod 1の数)をケースごとに用意する。
    modx_plus = x10 % (xcount1 + 1)
    if xcount1 == 1:
        modx_minus = 0
    else:
        modx_minus = x10 % (xcount1 - 1)
    popcount = defaultdict(int)
    for i1 in range(n):
        if x[i1] == '1':
            if xcount1 == 1:
                print(0)
                continue
            else:
                x3 = modx_minus - mod2minus[n - 1 - i1]
                if x3 < 0:
                    x3 += (xcount1 - 1)
                elif x3 > (xcount1 - 1):
                    x3 -= (xcount1 - 1)
                elif x3 == (xcount1 - 1):
                    print(1)
                    continue
        else:
            x3 = modx_plus + mod2plus[n - 1 - i1]
            if x3 < 0:
                x3 += (xcount1 + 1)
            elif x3 > (xcount1 + 1):
                x3 -= (xcount1 + 1)
            elif x3 == (xcount1 + 1):
                print(1)
                continue
        r = 1
        while x3:
            r += 1
            if popcount[x3] == 0:
                p = bin(x3).count('1')
                popcount[x3] = p
                x3 = x3 % p
            else:
                x3 = x3 % popcount[x3]
        print(r)

if __name__ == '__main__':
    main()