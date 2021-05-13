n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for yi, xi in enumerate(x):
    ans += min((xi) * 2, abs(k - xi) * 2)
print(ans)
