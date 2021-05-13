N = int(input())
P = [int(input())-1 for i in range(N)]

idx = [-1 for _ in range(N)]
successive = [False for _ in range(N)]

for i in range(N):
    idx[P[i]] = i

for p in P:
    if p < N-1 and idx[p+1] > idx[p]:
        successive[p] = True

cnt = 1
max_cnt = 0
for p in range(N):
    if successive[p]:
        cnt += 1
    else:
        max_cnt = max(cnt, max_cnt)
        cnt = 1

print(N-max_cnt)