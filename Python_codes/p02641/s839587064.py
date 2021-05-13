# C - Forbidden List

x, n = map(int,input().split())
P = list(map(int,input().split()))

t = -100
a = [0]*300
for p in P:
    a[100+p-1] = 1

d = 0
while True:
    if a[100+x-1-d] == 0:
        t = x-d
        break
    elif a[100+x-1+d] == 0:
        t = x + d
        break
    else:
        d += 1

print(t)
