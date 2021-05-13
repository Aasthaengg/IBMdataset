N = int(input())
A = [int(x) for x in input().split()]

SUM = sum(A)
ans = 0

for i in range(N+1):
    SUM -= A[i]
    if i == 0:
        res = min(1 - A[0], SUM)
    else:
        res = min(2*B-A[i], SUM)
    if res < 0:
        ans = -1
        break
    ans = ans + res + A[i] 
    B = res
    
print(ans)