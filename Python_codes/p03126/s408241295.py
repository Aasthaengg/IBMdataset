#B
n, m = map(int, input().split())
k = []
a = []
for i in range(n):
    l = list(map(int, input().split()))
    k.append(l[0])
    a.append(l[1:l[0] + 1])
# print(k, a)
ans = [0] * m
for i in range(n):
    b=k[i]
    for j in range(b):
        ans[a[i][j]-1] += 1
# print(ans)
count = 0
for i in range(m):
    if ans[i] == n:
        count += 1
print(count)