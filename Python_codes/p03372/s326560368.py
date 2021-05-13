n, c = map(int, input().split())
xv = [list(map(int, input().split())) for _ in range(n)]

# counter-clockwise
xv2 = []
for x, v in xv:
    xv2.append([c - x, v])
xv2 = xv2[::-1]

ans = 0

cumsum1, cumsum1_2 = [0], [0]
pos = 0
for x, v in xv:
    tmp = cumsum1[-1] + v - (x - pos)
    cumsum1.append(tmp)
    cumsum1_2.append(tmp - x)
    pos = x
    ans = max(ans, tmp)
cumsum1, cumsum1_2 = cumsum1[1:], cumsum1_2[1:]

cumsum2, cumsum2_2 = [0], [0]
pos = 0
for x, v in xv2:
    tmp = cumsum2[-1] + v - (x - pos)
    cumsum2.append(tmp)
    cumsum2_2.append(tmp - x)
    pos = x
    ans = max(ans, tmp)
cumsum2, cumsum2_2 = cumsum2[1:][::-1], cumsum2_2[1:][::-1]

tmpmax = 0
for i in reversed(range(n)):
    ans = max(ans, cumsum1[i] + tmpmax)
    tmpmax = max(tmpmax, cumsum2_2[i])

tmpmax = 0
for i in range(n):
    ans = max(ans, cumsum2[i] + tmpmax)
    tmpmax = max(tmpmax, cumsum1_2[i])

print(ans)
