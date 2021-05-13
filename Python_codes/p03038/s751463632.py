
N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

CB = []
for i in range(M):
    B, C = map(int, input().split())
    CB.append([C, B])
    
CB.sort(reverse=True)

idx = 0
c = 0
for i in range(N):
    if A[i] < CB[idx][0]:
        A[i] = CB[idx][0]
        c += 1
    if CB[idx][1] <= c:
        idx += 1
        c = 0
    if idx >= M:
        break
    #print(A)
        
print(sum(A))