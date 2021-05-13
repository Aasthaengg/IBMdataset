from math import gcd
from collections import Counter
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9+7

def main():
    N,*ab = map(int, read().split())

    ab_zero = 0
    ratio = []
    for a, b in zip(*[iter(ab)]*2):
        if a == 0 and b == 0:
            ab_zero += 1
        else:
            g = gcd(a, b)
            a //= g
            b //= g
            ratio.append((a, b))
    ab_zero %= MOD
    
    s = Counter(ratio)

    bad = 1
    for k, v in s.items():
        if v == 0:
            continue
        
        a, b = k
        if (-a, -b) in s:
            v += s[(-a, -b)]
            s[(-a, -b)] = 0

        inv = 0
        if (-b, a) in s:
            inv += s[(-b, a)]
            s[(-b, a)] = 0
        if (b, -a) in s:
            inv += s[(b, -a)]
            s[(b, -a)] = 0

        bad *= (pow(2, v, MOD) + pow(2, inv, MOD) -1) % MOD
        bad %= MOD
        s[k] = 0

    ans = (bad + ab_zero -1) % MOD
    print(ans)
    

if __name__ == "__main__":
    main()
