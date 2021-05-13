# coding: utf-8
# Your code here!
s=list(input())
X,Y=map(int,input().split())

if "T" in s:
    pass
else:
    if X==len(s) and Y==0:
        print("Yes")
    else:
        print("No")
    exit()


way=[[],[]]

switch=0
judge=True

lx=[]
ly=[0]
temp=0
for item in s:
    if item == "T":
        if judge:
            judge=False
            lx.append(temp)
        else:
            way[switch].append(temp)
        temp=0
        switch^=1
    else:
        temp+=1
way[switch].append(temp)

#print(lx)

for x in way[0]:
    temp_x=[]
    for item in lx:
        temp_x.append(item+x)
        temp_x.append(item-x)
    lx=temp_x[:]
    lx=list(set(lx))
#print(lx)

for y in way[1]:
    temp_y=[]
    for item in ly:
        temp_y.append(item+y)
        temp_y.append(item-y)
    ly=temp_y[:]
    ly=list(set(ly))
#print(ly)

if (X in lx) and (Y in ly):
    print("Yes")
else:
    print("No")