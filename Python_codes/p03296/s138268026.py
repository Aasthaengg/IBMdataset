n = int(input())
a = list(map(int, input().split()))

l = [1]
for i in range(1, n):
    if (a[i] == a[i - 1]):
        l[len(l) - 1] += 1
    else:
        l.append(1)

ans = 0
for ln in l:
    ans += ln // 2

print(ans)
