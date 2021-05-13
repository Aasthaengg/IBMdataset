N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

cnt = {}
for i in range(1, N+1):
    cnt[i] = 0

root = [0]
loop = []
now = 1
tmp = 0
amari = 0
while cnt[now] != 2:
    cnt[now] += 1
    root.append(now)
    if cnt[now] == 2:
        tmp = now
        break
    amari += 1
    now = A[now]

while cnt[tmp] == 2:
    loop.append(tmp)
    tmp = A[tmp]
    cnt[tmp] += 1

amari -= len(loop)

if K <= amari:
    ans = root[K+1]
else:
    ind = amari + (K-amari)%len(loop) + 1
    ans = root[ind]

print(ans)

