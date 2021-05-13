N = int(input())
A = [int(input()) for _ in range(N)]
        
x = 0
ans = 0
for i in range(N-1, -1, -1):
    if A[i] > x:
        ans += A[i]
        x = A[i]
    elif x > A[i]:
        ans = -1
        break
    x -= 1
if A[0] > 0:
    ans = -1    
print(ans)