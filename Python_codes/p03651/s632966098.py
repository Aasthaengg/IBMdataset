N,K = map(int, input().split())
As = list(map(int, input().split()))

def gcd(n, m):
    # 最大公約数
    a = max(n,m)
    b = min(n,m)
    while b:
        a, b = b, a % b
    return a

g = As[0]
for a in As:
    g = gcd(g, a)

for a in As:
    if a >= K and (a-K) % g == 0:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")