data = [int(n) for n in input().split(" ")];

def gcd(m, n):
    m = m % n;
    if m == 0:
        return n;
    return gcd(n, m);

print(gcd(max(data), min(data)));
