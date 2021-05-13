N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0

for i in range(N):
    if B[i] <= A[i]:
        ans += B[i]
    else:
        ans += A[i]
        remat = B[i]-A[i]
        if A[i+1] - remat < 0:
            ans += A[i+1]
        else:
            ans += remat
        
        A[i+1] = max(0,A[i+1]-remat)

print(ans)