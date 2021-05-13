h,w,a,b = map(int,input().split())
li = [[0]*w for _ in range(h)]

for i in range(b):
    for j in range(a):
        li[i][j] = 1
for i in range(b,h):
    for j in range(a,w):
        li[i][j] = 1

for i in range(h):
    for j in range(w):
        print(li[i][j],end = '')
    print()
