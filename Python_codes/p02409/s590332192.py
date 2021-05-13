n = int(input())
house = []
for i in range(4):
    house.append([])
    for j in range(3):
        house[i].append([])
        for k in range(10):
            house[i][j].append(0)

for i in range(n):
    b,f,r,v = map(int,input().split())
    house[b-1][f-1][r-1] += v


for i in range(4):
    for j in range(3):
        for k in range(10):
            print("" , house[i][j][k], end="")
        print()
    if i < 3:
        print("#" * 20)