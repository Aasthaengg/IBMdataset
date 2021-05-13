n = int(input())
*a, = map(int, input().split())

current = a[0]
ans = 0
for i in range(1, len(a)):
    if current == a[i]:
        ans += 1
        current = -1
    else:
        current = a[i]
print(ans)
