from collections import Counter

N = int(input())
A = list(map(int, input().split()))

A.sort()
A_counter = Counter(A)

dp = [True for _ in range(10**6+1)]
for a in A_counter:
    if dp[a] == False:
        continue
    for j in range(a*2, 10**6+1, a):
        dp[j] = False

c = 0
for a, v in A_counter.items():
    if dp[a] and v == 1:
        c += 1

print(c)
