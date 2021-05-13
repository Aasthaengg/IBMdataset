n, m = map(int, input().split())
if n%2 == 1:
    ans = []
    a = 1
    b = n-1
    for i in range(m):
        ans.append((a, b))
        a += 1
        b -= 1
else:
    ans = []
    a = 1
    b = n-1
    flag = True
    for i in range(m):
        if flag and b-a <= n//2:
            b -= 1
            flag = False
        ans.append((a, b))
        a += 1
        b -= 1
for i in range(m):
    print(*ans[i])
