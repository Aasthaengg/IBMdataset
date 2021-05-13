N = int(input())
a = list(map(int, input().split()))

ans = 0
for i, j in enumerate(a):
    if i % 2 == 0 and j % 2 == 1: ans += 1
print(ans)