n=int(input())
a=sorted([int(i) for i in input().split()])

def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
a=groupby(a)
#print(a)
l=len(a)
for i in range(l):
    if a[i][1]%2==0:
        a[i][1]=2
    else:
        a[i][1]=1
c=0
for i in range(l):
    if a[i][1]==2:
        c+=1
if c%2==0:
    print(l)
else:
    print(l-1)
