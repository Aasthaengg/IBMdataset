n = int(input())
A = list(map(int,input().split()))
A.sort()
ans = 1
m = A[0]
for i in range(n-1):
    if A[i+1] <= 2*m:
        ans += 1
    else:
        ans = 1
    m += A[i+1]
print(ans)