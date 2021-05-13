N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B.insert(0,0)
C = list(map(int,input().split()))
C.insert(0,0)
cnt = B[A[0]]
for i in range(1,N):
    if A[i]-A[i-1]==1:
        cnt += C[A[i-1]]
    cnt += B[A[i]]
print(cnt)