n = int(raw_input())
T = 0
H = 0

for i in range(n):
    t, h = raw_input().split()
    if t > h:
        T += 3
    elif t < h:
        H += 3
    else:
        T += 1
        H += 1

print("%d %d" % (T, H))