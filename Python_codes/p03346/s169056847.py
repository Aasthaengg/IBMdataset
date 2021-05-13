import bisect
n = int(input())
p = [int(input()) for _ in range(n)]
idx = dict()
for i in range(n):
    idx[p[i]] = i
c = 0
cnt = 1
for i in range(1, n):
    if idx[i + 1] > idx[i]:
        cnt += 1
    else:
        c = max(c, cnt)
        cnt = 1
c = max(c, cnt)
print(n - c)
