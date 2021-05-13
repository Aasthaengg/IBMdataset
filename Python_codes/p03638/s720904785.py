H, W = map(int, input().split(' '))
N = int(input())
A = list(map(int, input().split(' ')))

# A = [10, 5, 5, 3, 2]
# H, W = 5, 5

def get_position(H, W):
    for i in range(H):
        if i % 2 == 0:
            for j in range(W):
                yield i, j
        else:
            for j in range(W-1, -1, -1):
                yield i, j


buf = [['' for _ in range(W)] for _ in range(H)]
positions = get_position(H, W)
for c, a in enumerate(A):
    for _ in range(a):
        i, j = positions.__next__()
        # print(i, j)
        buf[i][j] = str(c+1)

for b in buf:
    print(' '.join(b))