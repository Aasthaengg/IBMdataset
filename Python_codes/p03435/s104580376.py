c = [list(map(int,input().split())) for i in range(3)]
#change
c1_2 = []
for i in range(3):
    c1_1 = []
    for j in range(2):
        c1_1.append(c[i][j] - c[i][j+1])
    c1_2.append(c1_1)
c1_1 = []
for i in range(3):
    for j in range(1):
        c1_1.append(c1_2[i][j] - c1_2[i][j+1])
if(len(set(c1_1))==1):
    print("Yes")
else:
    print("No")