import sys
import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
origin = sum(A)
heapq.heapify(A)

BC = [list(map(int, input().split())) for _ in range(M)]
BC = sorted(BC, reverse=True, key=lambda x: x[1])

count = 0

for i in range(M):
    b = BC[i][0]
    c = BC[i][1]
    for _ in range(b):
        smallest = heapq.heappop(A)
        tmp = c - smallest
        if tmp <= 0:
            heapq.heappush(A, smallest)
            break
        else:
            heapq.heappush(A, c)
            origin += tmp
            count += 1
            if count >= N:
                print(origin)
                sys.exit()

print(origin)
