from itertools import combinations as cb   
n = int(input())

k = 0
for i in range(1,1000):
    if i*(i-1)//2 == n:
        k = i
if k == 0:
    print("No")
    exit()

print("Yes")
print(k)
x = list(cb([i for i in range(k)], 2))
dp = [[] for i in range(k)]
for i,(a,b) in enumerate(x):
    dp[a].append(i+1)
    dp[b].append(i+1)
for r in dp:
    print(len(r), *r)