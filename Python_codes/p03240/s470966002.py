N = int(input())
Q = [list(map(int, input().split())) for _ in range(N)]
Q.sort(key=lambda x: x[2])
a, b, H = Q[-1]


def height(x, y, H, a, b):
    return max(H-abs(x-a)-abs(y-b), 0)


for i in range(101):
    for j in range(101):
        A = H+abs(i-a)+abs(j-b)
        B = height(a, b, H, i, j)
        f, g = True, True
        if not A:
            f = False
        if not B:
            g = False
        for k in range(N):
            x, y, h = Q[k]
            if height(i, j, A, x, y) != h:
                f = False
            if height(i, j, B, x, y) != h:
                g = False
            if not (f or g):
                break
        else:
            if f:
                print(i, j, A)
                exit()
            else:
                print(i, j, B)
                exit()
