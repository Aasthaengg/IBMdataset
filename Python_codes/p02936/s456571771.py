N, Q = map(int, input().split())

w = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    w[A].append(B)
    w[B].append(A)

cnt = [0]*(N+1)
for _ in range(Q):
    P, X = map(int, input().split())
    cnt[P] += X

flag = [False]*(N+1)

q = [1]
while q:
    n = q.pop()
    flag[n] = True
    for i in w[n]:
        if flag[i]:
            continue
        flag[i] = True
        cnt[i] += cnt[n]
        q.append(i)

print(" ".join([str(c) for c in cnt[1:]]))