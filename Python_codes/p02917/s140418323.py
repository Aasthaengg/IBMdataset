n = int(input())
b = [10 ** 9] + list(map(int, input().split())) + [10 ** 9]
ans = 0
for i in range(n):
    ans += min(b[i], b[i + 1])
print(ans)
