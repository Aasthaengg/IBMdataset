x, n = map(int, input().split())
p = list(map(int, input().split()))
xp =x; xm =x
for i in range(n+1):
    if not (xm in p):
        print(xm)
        break
    if not (xp in p):
        print(xp)
        break
    xp += 1
    xm -= 1