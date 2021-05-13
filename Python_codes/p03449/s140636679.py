from itertools import accumulate

N = int(input())
A = list(accumulate([int(i) for i in input().split()]))
B = list(accumulate([int(i) for i in input().split()][::-1]))[::-1]

ans = 0
for i in range(N):
    ans = max(ans,A[i]+B[i])

print(ans)
