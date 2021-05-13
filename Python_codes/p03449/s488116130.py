from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
SA = list(accumulate(A))
SB = list(accumulate(B))
ans = 0
for i in range(n):
    if i >= 1:
        ans = max(SA[i] + SB[n - 1] - SB[i - 1], ans)
    else:
        ans = max(SA[i] + SB[n - 1], ans)
print(ans)
