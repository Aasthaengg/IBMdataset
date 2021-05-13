N = int(input())
ans = 1
for i in range(1, N+1):
    ans *= i
    ans %= (1e9 + 7)

print(int(ans))