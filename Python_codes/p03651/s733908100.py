def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
g = arr[0]
for e in arr[1:]:
    g = gcd(g, e)

if k <= max(arr) and k//g*g == k:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")