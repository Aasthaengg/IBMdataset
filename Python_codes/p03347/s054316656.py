
N = int(input())
A = [int(input()) for _ in range(N)]
import sys
ans = 0
if A[0] != 0:
    print(-1)
    sys.exit()
for i in range(1,N):
    if A[i] - A[i-1] == 1:
        ans += 1
    elif A[i] <= A[i-1]:
        ans += A[i]
    else:
        print(-1)
        sys.exit()
    
print(ans)