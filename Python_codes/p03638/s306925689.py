def solve():
    H,W = map(int,input().split())
    N = int(input())
    A = list(map(int,input().split()))

    paint = []
    for i in range(N):
        paint += [i+1] * A[i]

    field = [[0] * W for _ in range(H)]

    w = 0
    toRight = True
    idx = 0
    for h in range(H):

        while 0 <= w < W:
            field[h][w] = str(paint[idx])
            idx += 1
            if toRight:
                w += 1
            else:
                w -= 1

        if toRight:
            toRight = False
            w = w-1
        else:
            toRight = True
            w = 0

    for i in range(H):
        print(" ".join(field[i]))

    
if __name__ == '__main__':
    solve()