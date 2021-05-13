N = int(input())
K = int(input())
x_li = list(map(int, input().split()))
ans = 0
for i in range(N):
    if x_li[i] > abs(K - x_li[i]):
        ans += 2 * abs(K - x_li[i])
    else:
        ans += 2*x_li[i]

print(ans)