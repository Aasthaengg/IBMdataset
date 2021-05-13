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
            if b < 0:
                a, b = -a, -b
            if b == 0:
                a = 1
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
        if (-b, a) in s:
            bad *= (pow(2, v, MOD) + pow(2, s[(-b, a)], MOD) -1) % MOD
            bad %= MOD            
            s[(-b, a)] = 0
        elif (b, -a) in s:
            bad *= (pow(2, v, MOD) + pow(2, s[(b, -a)], MOD) -1) % MOD
            bad %= MOD            
            s[(b, -a)] = 0
        else:
            bad *= pow(2, v, MOD)
            bad %= MOD            
        s[k] = 0

    ans = (bad + ab_zero -1) % MOD
    print(ans)
    

if __name__ == "__main__":
    main()
