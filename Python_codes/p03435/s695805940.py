x=[]
for i in range(3):
    x.append(list(map(int,input().split())))

flag=1
for i in range(2):
    if not(x[i+1][0]-x[i][0]==x[i+1][1]-x[i][1]==x[i+1][2]-x[i][2]):
        flag = 0
        break
if flag==1:
    print("Yes")
else:
    print("No")