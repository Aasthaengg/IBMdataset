from itertools import accumulate
n = int(input())
K = sorted(map(int,input().split()))
A = list(accumulate(K))
ans = 1
for i in range(n-2,-1,-1):
    if A[i]*2 >= K[i+1]:
        ans += 1
    else:
        break
print(ans)