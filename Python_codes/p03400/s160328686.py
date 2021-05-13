n = int(input())
d, k = map(int, input().split())
ans = 0
for i in range(n):
    x = int(input())
    ans += -(-d // x)

print(ans + k)
