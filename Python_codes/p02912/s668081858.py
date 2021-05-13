import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
A_dic = {} #value: idx
for i in range(N):
    if A[i] not in A_dic:
        A_dic[A[i]] = []
    A_dic[A[i]].append(i)

# その時の最大のAに１つ使う　これを繰り返す
total = 0
rest = M
if N == 1:
    while rest > 0:
        rest -= 1
        A[0] //= 2
    total = A[0]
elif N == 2:
    while rest > 0:
        rest -= 1
        if A[0] >= A[1]:
            A[0] //= 2
        else:
            A[1] //= 2
    total = A[0] + A[1]
else:
    hq = [-A[i] for i in range(N)]
    heapq.heapify(hq)
    while rest > 0:
    #     temp_idx = A_items[0][1]
    #     while A_items[0][0] >= A_items[1][0]:
    #         rest -= 1
    #         A_items[0][0] //= 2
    #         A[temp_idx] //= 2
    #     idx = 2
    #     while A_items[0][0] < A_items[idx][0]:
    #         idx += 1
    #         if idx >= N-1:
    #             break
    #     u, v = A_items[0], A_items[idx-1]
    #     A_items[idx-1] = u
    #     A_items[0] = v
    # total = sum(A)
        
        max_v = heapq.heappop(hq) * (-1)
        max_idx = A_dic[max_v].pop()
        A[max_idx] //= 2
        if max_v//2 not in A_dic:
            A_dic[max_v//2] = []
        A_dic[max_v//2].append(max_idx)
        heapq.heappush(hq, (max_v//2) * (-1))
        rest -= 1
    total = sum(A)
    


print(total)