H,W=map(int,input().split())
A=[]
for i in range(0,H):
    a=input()
    A.append(a)

alphabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

count=[0 for i in range(0,26)]

for i in range(0,H):
    for j in range(0,W):
        count[alphabetlist.index(A[i][j])]+=1

data=[0 for i in range(0,4)]

for i in range(0,26):
    data[count[i]%4]+=1

if H%2==0 and W%2==0:
    if data[1]==0 and data[2]==0 and data[3]==0:
        print('Yes')
    else:
        print('No')
elif H%2==0 and W%2==1:
    h=H//2
    if data[1]==0 and data[3]==0 and h>=data[2]:
        print('Yes')
    else:
        print('No')
elif H%2==1 and W%2==0:
    w=W//2
    if data[1]==0 and data[3]==0 and w>=data[2]:
        print('Yes')
    else:
        print('No')
else:
    if data[1]+data[3]>1:
        print('No')
    elif data[1]==1:
        h=(H-1)//2
        w=(W-1)//2
        if h+w>=data[2]:
            print('Yes')
        else:
            print('No')
    else:
        h=(H-1)//2
        w=(W-1)//2
        if h+w>=data[2]+data[3]:
            print('Yes')
        else:
            print('No')