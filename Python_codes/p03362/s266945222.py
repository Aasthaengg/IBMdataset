dp = [0]*55556
dp[0] = 1
dp[1] = 1
prime = []
for i in range(55556):
    if dp[i] == 0:
        prime.append(i)
        for j in range(i, 55556, i):
            dp[j] = 1
Enable = []
for i in prime:
    if i % 5 == 1:
        Enable.append(i)
N = int(input())
for i in Enable[:N]:
    print(i, end=" ")