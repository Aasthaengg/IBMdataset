n = int(input())
a = list(map(int , input().split()))
total = sum(a)
s = 0
ans = 10**10

for i in range(n - 1):
    s += a[i]
    t = total - s
    ans = min(ans, abs(s - t))

print(ans)