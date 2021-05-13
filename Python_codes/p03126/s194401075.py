n,m = map(int,input().split())
l = [0] * m
for i in range(n):
    a = list(map(int,input().split()))
    for j in a[1:]:
        l[j-1] += 1
ans = 0
for i in l:
    if i == n:
        ans += 1
print(ans)
