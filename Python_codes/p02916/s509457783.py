N = int(input())
A = input().split()
B = input().split()
C = input().split()

ans = 0
for i in range(N):
    ans+= int(B[i])

for i in range(N-1):
    if int(A[i])+1 ==int(A[i+1]):
        ans+=int(C[int(A[i])-1])

print(ans)