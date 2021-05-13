N = int(input())
a = list(map(int, input().split()))
xp = sum(a[::2]) - sum(a) // 2
ans = [xp * 2]
for i in range(N - 1):
    ans.append((a[i] - xp) * 2)
    xp = a[i] - xp
print(' '.join(list(map(str, ans))))