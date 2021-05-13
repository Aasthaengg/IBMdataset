n = int(input())
a = list(map(int, input().split()))

x1 = sum(a) - sum(a[1::2]) * 2

ans = []
ans.append(x1)
for i in range(n-1):
    ans.append(a[i]*2 - ans[i])

print(" ".join(map(str, ans)))