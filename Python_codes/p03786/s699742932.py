N = int(input())
A = list(map(int, input().split()))

A.sort()
import copy
cum = copy.copy(A)
for i in range(1,N):
    cum[i] = cum[i-1]+A[i]

def solve(A,cum,N):
    ans = 1
    for i in range(N-1,0,-1):
        if A[i]<=cum[i-1]*2:
            # print(A[i],cum[i-1])
            ans += 1
        else:
            break
    return ans
print(solve(A,cum,N))
