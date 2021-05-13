a=[]
for _ in range(3): a.append(list(map(int,input().split())))
n=int(input())
for _ in range(n):
    b=int(input())
    for i in range(3):
        for j,val in enumerate(a[i]):
            if val==b: a[i][j]=0

for i in range(3):
    if a[i]==[0,0,0]:
        print("Yes")
        exit()
    if a[0][i]==0 and a[1][i]==0 and a[2][i]==0:
        print("Yes")
        exit()
if a[0][0]==0 and a[1][1]==0 and a[2][2]==0:
    print("Yes")
    exit()
if a[0][2]==0 and a[1][1]==0 and a[2][0]==0:
    print("Yes")
    exit()
print("No")