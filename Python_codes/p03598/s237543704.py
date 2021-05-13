N = int(input())
K = int(input())
X = list(map(int, input().split()))
ans = 0
for xi in X:
    ans += min(xi, (K-xi))*2
print(ans)