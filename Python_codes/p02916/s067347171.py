N = int(input().rstrip())
A = list(map(int,input().rstrip().split()))
B = list(map(int,input().rstrip().split()))
C = list(map(int,input().rstrip().split()))
ans = sum(B)
for i in range(N-1):
    if A[i]+1 == A[i+1]:
        ans += C[A[i]-1]
print(ans)