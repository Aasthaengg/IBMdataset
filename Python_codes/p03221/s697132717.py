import heapq

N, M = map(int, input().split())
P_list = []
ans = []

for i in range(N+1):
    P_list.append([])

for i in range(M):
    P, Y = map(int, input().split())
    Y = Y * 10 ** 6 + i
    P_list[P].append(Y)

for i in range(N+1):
    P_list[i].sort()
    for j, k in enumerate(P_list[i]):
        tmp = (k % 10**6 + 1) * 10**12 + i * 10**6 + j + 1
        ans.append(tmp)

heapq.heapify(ans)

for i in range(M):
    pr = heapq.heappop(ans)
    ans_pr = str(pr % 10**12)
    print(ans_pr.zfill(12))