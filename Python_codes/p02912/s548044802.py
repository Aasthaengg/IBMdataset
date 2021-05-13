import heapq

I = input().split()
N = int(I[0])
M = int(I[1])
# N: 品物の数
# M: 割引券の数
# A: 品物の値段行列
A = list(map(int , input().split()))

A = list(map(lambda x: x*(-1), A))

heapq.heapify(A)
for i in range(M):
    M -= 1
    pri = heapq.heappop(A)

    pri *= -1
    pri //= 2
    pri *= -1

    heapq.heappush( A , pri )

Fi_pri = 0
for i in range(N):
    Fi_pri += A[i]

print( -1 * Fi_pri )