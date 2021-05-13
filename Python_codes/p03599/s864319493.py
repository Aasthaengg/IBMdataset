import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    A, B, C, D, E, F = map(int, input().split())
    water = [0]*F**2
    sugar = [0]*F**2

    sugar_idx = 0
    for i in range(F+1):
        for j in range(F+1):
            y = i*C+j*D
            if y <= F:
                sugar[sugar_idx] = y
                sugar_idx += 1

    water_idx = 0
    for i in range(F+1):
        for j in range(F+1):
            x = i*100*A+j*200*D
            if x <= F:
                water[water_idx] = x
                water_idx += 1

    dens = 0
    ans = (0, 0)

    for i in range(water_idx):
        for j in range(sugar_idx):
            w=water[i]
            s=sugar[j]
            if 0 < w+s <= F:
                if s/(w+s) >= dens and s/(w+s) <= E/(100+E):
                    dens = s/(w+s)
                    ans = (w+s, s)
    print(*ans)


resolve()