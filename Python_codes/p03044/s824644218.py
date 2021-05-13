import collections

N = int(input())

UVW = [[int(x) for x in input().split()] for _ in range(N - 1)]


ans = [-1] * N

A = [[] for _ in range(N)]


for u, v, w in UVW:
    A[u - 1].append([v - 1, w % 2])
    A[v - 1].append([u - 1, w % 2])

q = collections.deque()
q.append(0)

ans[0] = 0
while q:
    c = q.popleft()

    for ni, nd in A[c]:
        if ans[ni] != -1:
            continue

        if nd == 0:
            ans[ni] = ans[c]
        else:
            ans[ni] = ans[c] ^ 1

        q.append(ni)

if sum(ans) == 0:
    ans[0] = 1

for a in ans:
    print(a)



