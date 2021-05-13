n = int(input())
d, x = map(int, input().split())

ans = x

for a in range(0, n):
    A = int(input())
    ans += int((d - 1)/A) + 1

print(ans)
