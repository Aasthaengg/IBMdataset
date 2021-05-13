N, M = map(int, input().split())
a = [0 for i in range(M)]
b = [0 for i in range(M)]
cnt = [0 for i in range(N)]

for i in range(M):
    a[i], b[i] = map(int, input().split())

for i in range(M):
    cnt[a[i]-1] += 1
    cnt[b[i]-1] += 1

for i in range(N):
    print(cnt[i])