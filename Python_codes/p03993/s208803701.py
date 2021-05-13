n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    opp = a[a[i - 1] - 1]
    if i == opp:
        ans += 1
print(ans // 2)
