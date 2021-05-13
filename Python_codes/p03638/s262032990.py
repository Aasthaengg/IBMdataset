H, W = map(int, input().split())
N = int(input())
a = [int(i) for i in input().split()]
ary = [[0]*W for _ in range(H)]
s = 1
h, w = 0, 0
for i, n in enumerate(a):
    while n > 0:
        ary[h][w] = i+1
        w += s
        if w < 0:
            w = 0
            s = 1
            h += 1
        elif w >= W:
            h += 1
            w = W-1
            s = -1
        n -= 1
for a in ary:
    print(*a)
