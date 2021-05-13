n = int(input())
ans = 0
for x in range(n):
    l, r = map(int, input().split())
    ans += r - l + 1
print(ans)