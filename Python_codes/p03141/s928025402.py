n = int(input())
ans, a, b = 0, [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x+y)
    b.append([x, y])
num = [x for x in range(n)]
a, a0 = zip(*sorted(zip(a, num)))
a, a0 = list(a), list(a0)

for i in range(n):
    val = a0.pop()
    a.pop()
    if i%2 == 0:
       ans += b[val][0]
    else:
       ans -= b[val][1]
print(ans)
