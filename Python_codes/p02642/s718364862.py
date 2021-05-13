#template
def inputlist(): return [int(j) for j in input().split()]
#template
ans = 0
from collections import Counter
N = int(input())
A = inputlist()
A.sort()
dic = Counter(A)
dp = [1 for _ in range(A[-1]+1)]
for i in range(N):
    if dp[A[i]]:
        j = 2
        while A[i]*j <= A[-1]:
            dp[A[i]*j] = 0
            j +=1
        if dic[A[i]] == 1:
            ans+=1
print(ans)