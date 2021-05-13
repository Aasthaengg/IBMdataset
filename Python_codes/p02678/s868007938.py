from collections import deque
N, M = list(map(int, input().split()))
S = [set() for _ in range(N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    S[a].add(b)
    S[b].add(a)
# print(S)

parents = [-1]*N
parents[0] = 0
L = deque([0])
while L:
    k = L.pop()
    s=S[k]
    for l in s:
        if parents[l] < 0:
            L.appendleft(l)
            parents[l] = k
    # print(L)

if -1 in parents:
    print('No')
else:
    print('Yes')
    for i in range(1, N):
        print(parents[i]+1)