from math import gcd
import sys
input = sys.stdin.readline

def main():
    n = int(input())

    dict1 = {}
    mod = 1000000007
    cnt00 = 0
    cnt01 = 0
    cnt10 = 0

    for _ in range(n):
        a,b = map(int,input().split())
        if a == 0 and b == 0:
            cnt00 += 1
        elif a == 0:
            cnt01 += 1
        elif b == 0:
            cnt10 += 1
        else:
            c = gcd(a,b)
            if b < 0:
                a *= -1
                b *= -1
            set1 = (a//c, b//c)
            if set1 in dict1:
                dict1[set1] += 1
            else:
                dict1[set1] = 1

    ans = 1

    for k,v in dict1.items():
        a,b = k
        if dict1[(a,b)] == -1:
            continue
        if a > 0:
            if (-b,a) in dict1:
                ans *= 2**v + 2**dict1[(-b,a)] - 1
                dict1[(-b,a)] = -1
            else:
                ans *= 2**v
        else:
            if (b,-a) in dict1:
                ans *= 2**v + 2**dict1[(b,-a)] - 1
                dict1[(b,-a)] = -1
            else:
                ans *= 2**v
        ans %= mod

    ans *= 2 ** cnt01 + 2 ** cnt10 - 1
    ans += cnt00 - 1

    print(ans%mod)

if __name__ == '__main__':
    main()
