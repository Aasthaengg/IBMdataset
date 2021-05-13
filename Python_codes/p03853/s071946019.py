h,w = map(int,input().split())
m = list(list(input()) for i in range(h))

portrait = []
for i in range(2*h):
    for j in range(w):
        print(m[int(i/2)][j], end='')
    print()

