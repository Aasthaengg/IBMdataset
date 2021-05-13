import math
n, h = map(int,input().split())
am = 0
b = [0 for i in range(n)]

for i in range(n):
    ai,bi = map(int,input().split())
    if ai > am:
        am = ai
    b[i] = bi

b.sort(reverse=True)
ans = n

for i,bi in enumerate(b):
    if bi > am:
        h -= bi
        if h <= 0:
            print(i+1)
            exit()
    else:
        ans = i
        break

ans += math.ceil(h/am)
print(ans)
