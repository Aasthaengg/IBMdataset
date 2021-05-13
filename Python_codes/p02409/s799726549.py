buildings=[[[0 for i in range(10)]for m in range(3)]for k in range(4)]
x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    buildings[a-1][b-1][c-1]+=d
for i in range(4):
    for j in range(3):
        for k in range(10):
            print("",buildings[i][j][k],end="")
        print()
    if i!=3:
        print("#"*20)