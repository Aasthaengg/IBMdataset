N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
A.insert(0,0)
C = {i:0 for i in range(1,N+1)}
for i in range(2,N+1):
    a = A[i]
    C[a] += 1
for i in range(1,N+1):
    print(C[i])