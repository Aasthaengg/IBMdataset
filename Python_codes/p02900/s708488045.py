from collections import Counter

def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

def pf(N):
    res = []
    x = N
    y = 2
    while y*y <= x:
        while x % y == 0:
            res.append(y)
            x //= y
        y += 1
    if x > 1:
        res.append(x)
    return res

def main():
    a, b = map(int, input().split())
    print(len(Counter(pf(gcd(a,b))))+1)

if __name__ == "__main__":
    main()