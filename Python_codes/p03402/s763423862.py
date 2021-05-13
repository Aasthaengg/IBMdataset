A,B=map(int,input().split())
l=[[0]*100 for i in range(40)]
A-=1
for i in range(0,19,2):
    for j in range(1,100,2):
        if A:
            l[i][j]=1
            A-=1
B-=1
for i in range(21,40,2):
    for j in range(1,100,2):
        if B:
            l[i][j]=1
            B-=1
print(40,100)
for i in l[:20]:
    for j in i:
        print("." if j else "#",end="")
    print()
for i in l[20:]:
    for j in i:
        print("#" if j else ".",end="")
    print()