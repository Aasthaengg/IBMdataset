n = int(input())
h = [int(xi) for xi in input().split()]

step = 0
mstep = 0
for xi in range(n-1):
    if h[xi] >= h[xi+1]:
        step += 1
    else:
        if mstep<step:
            mstep = step
        step = 0

if mstep<step:
    mstep = step

print(mstep)
