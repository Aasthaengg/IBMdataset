n, k = map(int, input().split())

ans = 1
for i in range(n):
    ans = ans*k if i == 0 else ans*(k-1)

print(ans)