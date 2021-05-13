n, m = map(int, input().split())
q = list()
for i in range(m):
    q.append(list(map(int, input().split())))
p = list(map(int, input().split()))

ans = 0

for s in range(2**n):
    judge = True
    for i in range(m):
        cnt = 0
        for j in range(1, len(q[i])):
            w = q[i][j]
            if s >>(w-1) & 1 == 1:
                cnt += 1
        if cnt % 2 != p[i]:
            judge = False
    if judge:
        ans += 1
print(ans)