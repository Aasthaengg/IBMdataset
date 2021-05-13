N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
C.append(0)

for i in range(1, N+1):
    if i == N:
        break
    if A[i-1]+1 == A[i]:
        B.append(C[A[i-1]-1])
    
print(sum(B))