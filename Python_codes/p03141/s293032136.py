n = int(input())
l = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    l[i] = (a + b, a, b)
ans = 0
l.sort(reverse=True)
for i in range(n):
    if i % 2:
        ans -= l[i][2]
    else:
        ans += l[i][1]
print(ans)
