n = int(input())
H = list(map(int, input().split()))
DP = [0 for i in range(n)]

DP[0] = 0
DP[1] = abs(H[1] - H[0])
for i in range(2, n):
    a = DP[i - 2] + abs(H[i] - H[i - 2])
    b = DP[i - 1] + abs(H[i] - H[i - 1])
    if a <= b:
        DP[i] = a
    else:
        DP[i] = b
print(DP[n - 1])