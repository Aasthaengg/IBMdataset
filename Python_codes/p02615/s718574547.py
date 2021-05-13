N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = A[-1]
if N%2==0:
    for i in range(1,(N-2)//2+1):
        ans += A[N-1-i]*2
else:
    for i in range(1,(N-2)//2+1):
        ans += A[N-1-i]*2
    ans += A[N-2-i]
print(ans)