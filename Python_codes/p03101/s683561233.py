h = [input().split() for l in range(2)]
a = (int)(h[0][0])
b = (int)(h[1][0])
c = (int)(h[0][1])
d = (int)(h[1][1])
ans = (a - b) * (c - d)
print(ans)