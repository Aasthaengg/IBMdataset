#two alpinist
N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
mod = 10**9+7
 
#fixed[i]: i 山の高さが確定してる
fix_a= [0]*(N)
fix_b= [0]*(N)
fix_a[0] = A[0]
fix_b[-1] = B[-1]
for i in range(N-1):
    if A[i+1]>A[i]:
        fix_a[i+1] = A[i+1]
    if B[-(i+2)]>B[-(i+1)]:
        fix_b[-(i+2)] = B[-(i+2)]

ans = 1
for i in range(N):
    if fix_a[i]:
        if B[i]<fix_a[i]:
            ans = 0
            break
    if fix_b[i]:
        if A[i]<fix_b[i]:
            ans = 0
            break
            
for i in range(N):
    if fix_a[i] or fix_b[i]:
        continue
    ans *= min(A[i], B[i])
    ans %= mod
    
if A[-1] != B[0]:
    ans = 0
    
print(ans)

