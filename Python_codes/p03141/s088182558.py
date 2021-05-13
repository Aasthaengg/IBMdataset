n = int(input())
happy = []
for i in range(n):
    happy.append(tuple(map(int, input().split())))
happy.sort(key=sum, reverse=True)
ans = 0
for i, (a, b) in enumerate(happy):
    if i % 2 == 0:
        ans += a
    else:
        ans -= b
print(ans)
