N = int(input())
A,B = [0]*N,[0]*N
for i in range(N):
    A[i],B[i] = map(int,input().split())
A = sorted(A)
B = sorted(B)
if N%2 == 1:
    ans = B[int((N-1)/2)] - A[int((N-1)/2)] + 1
elif N%2 == 0:
    ans = B[int(N/2)] + B[int(N/2-1)] - A[int(N/2)] - A[int(N/2-1)] + 1
print(ans)