N = int(input())
low = 10 ** 6
ans = 0
for p in map(int, input().split()):
    if p <= low:
        low = p
        ans += 1
print(ans)
