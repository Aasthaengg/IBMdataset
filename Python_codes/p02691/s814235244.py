from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# j-i == A[i]+A[j] (i < j)                                                                                                                                                                                                                    
# A[i]+i == j-A[j]                                                                                                                                                                                                                            

memo = defaultdict(int)

ans = 0
for i in range(N):
    target = i - A[i]
    ans += memo[target]
    memo[A[i]+i] += 1
print(ans)