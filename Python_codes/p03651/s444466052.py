def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = max(a)
for i in range(1, n):
    a[i] = gcd(a[i], a[i - 1])
print("POSSIBLE" if k % a[n - 1] == 0 and k <= m else "IMPOSSIBLE")