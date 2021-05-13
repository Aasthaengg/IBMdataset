from collections import defaultdict
import math

def main():
    MOD = 10**9+7
    N = int(input())
    zero_cnt = 0
    L = defaultdict(int)
    L2 = defaultdict(int)
    for _ in range(N):
        x,y = map(int,input().split())
        if x == 0 and y == 0:
            zero_cnt += 1
            continue
        d = math.gcd(x,y)
        x //= d
        y //= d
        if x == 0 and y == 0:
            zero_cnt += 1
        if y < 0:
            x *= -1
            y *= -1
        elif ｙ == 0 and ｘ < 0:
            x *= -1
            y *= -1
        rot90 = (x <= 0)
        if rot90:
            tmp = x
            x = y
            y = -tmp
        if rot90:
            L[(x,y)] += 1
        else:
            L2[(x,y)] += 1

    ans = 1
    keys = set(list(L.keys()) + list(L2.keys()))
    for k in keys:
        now = 1
        s = L[k]
        t = L2[k]
        now += pow(2,s,MOD) - 1
        now += pow(2,t,MOD) -1
        ans *= now
        ans %= MOD
    ans -= 1
    ans += zero_cnt
    print(ans%MOD)

main()