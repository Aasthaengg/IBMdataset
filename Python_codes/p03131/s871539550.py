k, a, b = map(int, input().split())

if b - a <= 2 or k-(a-1) <= 0:
    ans = 1 + k
else:
    k = k - (a-1)
    n = k // 2
    ans = (n-1) * (b-a) + b + (k-2*n)
print(ans)