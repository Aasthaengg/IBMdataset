n = int(input())
a = list(map(int, input().split()))

x = 1
ans = 0

if not 1 in a:
    ans = -1
else:
    for i, item in enumerate(a):
        if item == x:
            x += 1
        else:
            ans += 1

print(ans)
