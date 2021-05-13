N, *A = map(int, open(0).read().split())

A = [a - 1 for a in A]
cur = 0
cnt = 0
for _ in range(N):
    nxt = A[cur]
    cnt += 1
    if nxt == 1:
        print(cnt)
        break
    cur = nxt
else:
    print(-1)
