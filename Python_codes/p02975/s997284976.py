from itertools import groupby

N=int(input())
A=list(map(int,input().split()))
A.sort()
X=groupby(A)
data=[]
for key,group in X:
    g=len(list(group))
    data.append([key,g])
if len(data)==1 and data[0][0]==0:
    print('Yes')
elif N%3!=0:
    print('No')
else:
    if len(data)>3:
        print('No')
    elif len(data)==1:
        if data[0][0]==0:
            print('Yes')
        else:
            print('No')
    elif len(data)==2:
        if data[0][0]==0 and data[0][1]==N//3:
            print('Yes')
        else:
            print('No')
    else:
        if data[0][1]!=N//3 or data[1][1]!=N//3 or data[2][1]!=N//3:
            print('No')
        else:
            if data[0][0]^data[1][0]^data[2][0]!=0:
                print('No')
            else:
                print('Yes')