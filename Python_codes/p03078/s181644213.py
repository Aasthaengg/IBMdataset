import heapq

x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B, reverse=True)
C = sorted(C, reverse=True)

hq = []
heapq.heapify(hq)
i, j, l = 0, 0, 0

heapq.heappush(hq, [(A[i]+B[j]+C[l])*-1, i, j, l])
Used = []

for i in range(k):
    now = heapq.heappop(hq)
    print(now[0]*-1)
    i = now[1]
    j = now[2]
    l = now[3]

    if i >= x-1:
        pass
    elif [(A[i+1]+B[j]+C[l])*-1, i+1, j, l] not in Used:
        Used.append([(A[i+1]+B[j]+C[l])*-1, i+1, j, l])
        heapq.heappush(hq, [(A[i+1]+B[j]+C[l])*-1, i+1, j, l])
        
    if j >= y-1:
        pass
    elif [(A[i]+B[j+1]+C[l])*-1, i, j+1, l] not in Used:
        Used.append([(A[i]+B[j+1]+C[l])*-1, i, j+1, l])
        heapq.heappush(hq, [(A[i]+B[j+1]+C[l])*-1, i, j+1, l])
        
    if l >= z-1:
        pass
    elif [(A[i]+B[j]+C[l+1])*-1, i, j, l+1] not in Used:
        Used.append([(A[i]+B[j]+C[l+1])*-1, i, j, l+1])
        heapq.heappush(hq, [(A[i]+B[j]+C[l+1])*-1, i, j, l+1])
        
    # print(hq)