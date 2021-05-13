# coding: utf-8
# Your code here!

N = int(input())
C = []

prev = -1

for _ in range(N):
    tmp = int(input())
    if tmp != prev:
        C.append(tmp)
    prev = tmp

dp = [0]*(len(C)+1)
place = {}
dp[0] = 1

for i in range(len(C)):
    if place.get(C[i]) != None:
        dp[i+1] = dp[i] + dp[place.get(C[i])]
    else:
        dp[i+1] = dp[i]
    place[C[i]] = i+1
    
print(dp[-1]%(10**9+7))