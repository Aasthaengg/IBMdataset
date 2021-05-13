n=int(input())
x1=[[int(0) for i in range(10)]for j in range(3)]
x2=[[int(0) for i in range(10)]for j in range(3)]
x3=[[int(0) for i in range(10)]for j in range(3)]
x4=[[int(0) for i in range(10)]for j in range(3)]

for i in range(n):
    b,f,r,v=[int(s) for s in input().split()]
    if b==1:
        x1[f-1][r-1]=x1[f-1][r-1]+v
    elif b==2:
        x2[f-1][r-1]=x2[f-1][r-1]+v
    elif b==3:
        x3[f-1][r-1]=x3[f-1][r-1]+v
    else:
        x4[f-1][r-1]=x4[f-1][r-1]+v
for j in range(3):
    for k in range(10):
        print("",x1[j][k],end="")
    print("")
for n in range(20):
    print('#',end="")
print("")
for j in range(3):
    for k in range(10):
        print("",x2[j][k],end="")
    print("")
for n in range(20):
    print('#',end="")
print("")
for j in range(3):
    for k in range(10):
        print("",x3[j][k],end="")
    print("")
for n in range(20):
    print('#',end="")
print("")
for j in range(3):
    for k in range(10):
        print("",x4[j][k],end="")
    print("")