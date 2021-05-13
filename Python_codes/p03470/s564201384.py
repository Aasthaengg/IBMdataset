N = int(input())
d = [0 for _ in range(N)]
for i in range(N):
    d[i] = int(input())

d = sorted(d)

cnt = 0
max = 0
for i in range(len(d)):
    if max < d[i]:
        max = d[i]
        cnt += 1
print(cnt)
