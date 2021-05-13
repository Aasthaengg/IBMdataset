N = int(input())
a = []
for i in range(3):
    a.append(input())

ans = 0
for i in range(N):
    if a[0][i] != a[1][i] and a[1][i] != a[2][i] and a[0][i] != a[2][i]:
        ans += 2
    elif a[0][i] == a[1][i] and a[1][i] == a[2][i] and a[0][i] == a[2][i]:
        continue
    else:
        ans += 1
print(ans)