N=int(input())
a=[0]*N
b=[0]*N
genzai=0
AB=[]
for i in range(N):
    A,B=map(int,input().split())
    a[i]=A
    b[i]=B
    AB.append([B,A])
AB.sort()
for i in range(N):
    genzai+=AB[i][1]
    if genzai>AB[i][0]:
        print("No")
        exit()
print("Yes")