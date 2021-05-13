from itertools import *
N,C=map(int,input().split())
D=[list(map(int,input().split())) for i in range(C)]
c=[list(map(int,input().split())) for i in range(N)]

lst=[[],[],[]]

for y in range(N):
    for x in range(N):
        lst[(y+x)%3].append(c[y][x])


Revalue=10**18

valuelst=[[0 for i in range(C)] for i in range(3)]
for v in range(3):
    for Color in range(1,C+1):
        value=0
        for i in lst[v]:
            value+=D[i-1][Color-1]
        valuelst[v][Color-1]=value


for Color1,Color2,Color3 in list(permutations(list(range(1,C+1)),3)):
    value=valuelst[0][Color1-1]+valuelst[1][Color2-1]+valuelst[2][Color3-1]

    Revalue=min(Revalue,value)
print(Revalue)
