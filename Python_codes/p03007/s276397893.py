N = int(input())
A = list(map(int,input().split()))
A.sort()
p = 0
ans = -A[0]
for i in range(1,N-1):
    if A[i] < 0:
        p += 1
        ans -= A[i]
    else:
        ans += A[i]
ans += A[-1]
print(ans)
for i in range(p+1,N-1):
    print(A[p],A[i])
    A[p] -= A[i]
for i in range(p+1):
    print(A[-1],A[i])
    A[-1] -= A[i]
