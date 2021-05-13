N = int(input())
a = list(map(int,input().split()))

res = 10**12
n = sum(a)
x = 0
for i in range(N-1):
    x += a[i]
    y = n - x
    ans = abs(x-y)
    res = min(res,ans)
print(res)