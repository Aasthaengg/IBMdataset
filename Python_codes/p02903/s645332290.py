h,w,a,b=map(int,input().split())

#行に含まれる数はa、列に含まれる数はb
#行の並び替えは可能
#列の並び替えも可能

if b>h//2:
    print("No")
    exit()
if a>w//2:
    print("No")
    exit()


mapss=[[0]*w for _ in range(h)]

for y in range(b):
    for x in range(a):
        mapss[y][x]=1

for y in range(b,h):
    for x in range(a,w):
        mapss[y][x]=1


for item in mapss:
    print("".join(map(str,item)))