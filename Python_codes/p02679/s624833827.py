import sys

def main():
    input = sys.stdin.readline
    mod = pow(10,9)+7
    
    n = int(input())
    key1 = dict()
    key2 = dict()
    
    a_0 = 0
    b_0 = 0
    ab_0 = 0
    
    for i in range(n):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            ab_0 += 1
            continue
        if a == 0:
            a_0 += 1
            continue
        if b == 0:
            b_0 += 1
            continue
        k1, k2 = abs(a), abs(b)
        if k2 < k1:
            k1, k2 = k2, k1
        while k2%k1:
            k2, k1 = k1, k2%k1
        a //= k1
        b //= k1
        if a*b > 0:
            k = (abs(a), abs(b))
            if k in key1:
                key1[k] += 1
            else:
                key1[k] = 1
        else:
            k = (abs(b), abs(a))
            if k in key2:
                key2[k] += 1
            else:
                key2[k] = 1
    
    
    left = n-a_0-b_0-ab_0
    key = [(a_0, b_0)]
    for k, v in key1.items():
        if k in key2:
            v2 = key2[k]
            key.append((v, v2))
            left -= v+v2
    
    ans = pow(2, left, mod)
    for a, b in key:
        ans *= pow(2, a, mod)+pow(2, b, mod)-1
        ans %= mod
    ans += mod-1
    ans += ab_0
    ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()

