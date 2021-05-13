N = int(input())
K = int(input())
x = list(map(int,input().split()))

ans = 0
for xi in x:
    if 2*xi <= 2 * (K - xi):
        ans += 2 * xi
    else:
        ans += 2 * (K - xi)
print(ans)