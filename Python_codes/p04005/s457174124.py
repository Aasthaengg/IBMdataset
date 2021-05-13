a = list(map(int, input().split()))
a.sort()
ans = a[0] * a[1]

for i in a:
    if i % 2 == 0:
        ans = 0
        break

print(ans)