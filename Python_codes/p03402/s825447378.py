h, w = 66, 65
a, b = map(int,input().split())

c = [['#' if i < h//2 else '.']*w for i in range(h)]

for i in range(a-1):
    c[i//((h-1)//2)*2+1][i%((h-1)//2)*2+1] = '.'
for i in range(b-1):
    c[i//((h-1)//2)*2+h//2+1][i%((h-1)//2)*2+1] = '#'


print(h,w)
for i in range(h):
    for j in range(w):
        print(c[i][j],end='')
    print()
