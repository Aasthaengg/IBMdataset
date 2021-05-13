X = int(input())
DP = [0]*100001
DP[100] = 1
DP[101] = 1
DP[102] = 1
DP[103] = 1
DP[104] = 1
DP[105] = 1

for i in range(106, 100001):
    if any([DP[i-100], DP[i-101], DP[i-102], DP[i-103], DP[i-104], DP[i-105]]):
        DP[i] = 1
print(DP[X])