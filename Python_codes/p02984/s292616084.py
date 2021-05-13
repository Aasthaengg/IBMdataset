n = int(input())
a = list(map(int, input().split()))
s = sum(a)
res = s
for i in range(n):
    if i%2 == 1:
        res -= 2*a[i]
ans = []
ans.append(str(res))
tmp = res
for i in range(n-1):
    now = 2*a[i] - tmp
    ans.append(str(now))
    tmp = now
print(" ".join(ans))