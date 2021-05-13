n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b):
    print('-1')
    exit()

c = []
t = 0
ans = 0
for x, y in zip(a, b):
    if x < y:
        t += y - x
        ans += 1
    else:
        c.append(x - y)

if ans == 0:
    print('0')
    exit()

c.sort(reverse=True)
for p in c:
    t -= p
    ans += 1
    if t < 0:
        break
print(ans)
