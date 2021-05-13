# B - Collecting Balls (Easy Version)

N = int(input())
K = int(input())
X = list(int(x) for x in input().split())

ans = 0
for x in X:
    ans += min(x, K-x) * 2
print(ans)