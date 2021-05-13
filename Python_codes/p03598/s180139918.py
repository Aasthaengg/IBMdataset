

N = int(input())
K = int(input())
x = [int(x) for x in input().split()]
ans = 0
for i in range(N):
    ans += min(x[i] * 2, abs(K - x[i]) * 2)
print(ans)