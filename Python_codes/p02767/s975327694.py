N = int(input())
X = list(map(int, input().split()))

ans = 10**18
ans_ = 0

for P in range(1, max(X) + 1):
    ans_ = 0
    for x in X:
        ans_ += (x - P) ** 2
    ans = min(ans, ans_)

print(ans)
