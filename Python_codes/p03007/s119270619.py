N=int(input())
A=list(map(int,input().split()))

A.sort(reverse=True)
P=[]
M=[]

for i in A:
    if i<0:
        M.append(i)
    else:
        P.append(i)

ans=[]
if len(M)==0:
    if P[0]==0:
        print(0)
        for i in range(N-1):
            print(0,0)
        exit()
    else:
        x=P.pop()
        y=P.pop(0)
        ans.append([x,y])
        M.append(x-y)
if len(P)==0:
    x=M.pop(0)
    y=M.pop()
    ans.append([x,y])
    P.append(x-y)


for i in range(len(P)-1):
    y=P.pop()
    x=M.pop()
    ans.append([x,y])
    M.append(x-y)

for i in range(len(M)):
    y=M.pop()
    x=P.pop()
    ans.append([x,y])
    P.append(x-y)

print(P[0])

for x,y in ans:
    print(x,y)





