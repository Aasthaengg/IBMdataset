n = int(input())

AB = [[0, 0, 0] for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    AB[i][0] = a+b
    AB[i][1] = a
    AB[i][2] = b

AB.sort()
ans = 0
for i in range(n):
    _, a, b = AB.pop()
    if i%2 == 0:
        ans += a
    else:
        ans -= b
print(ans)