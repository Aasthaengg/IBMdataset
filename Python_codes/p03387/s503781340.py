l = list(map(int, input().split()))

l.sort()

ans = 0

if (l[2] - l[0]) % 2 == 1:
    ans += (l[2] - l[0]) // 2
    l[0] = l[2] - 1
else:
    ans += (l[2] - l[0]) // 2
    l[0] = l[2]

if (l[2] - l[1]) % 2 == 1:
    ans += (l[2] - l[1]) // 2
    l[1] = l[2] - 1
else:
    ans += (l[2] - l[1]) // 2
    l[1] = l[2]

if l[0] == l[1] == l[2] - 1:
    print(ans + 1)
elif l[0] == l[1] == l[2]:
    print(ans)
else:
    print(ans + 2)