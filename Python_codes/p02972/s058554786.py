N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
B = [0 for _ in range(N+1)]
for i in range(N//2+1,N+1):
    B[i] = A[i]
for i in range(N//2,0,-1):
    cnt = A[i]
    for j in range(2,N//i+1):
        cnt = (cnt+B[i*j])%2
    B[i] = cnt
C = []
for i in range(1,N+1):
    if B[i]==1:
        C.append(i)
print(len(C))
print(*C)