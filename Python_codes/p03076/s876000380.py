import math
a=[]
first=[]
for i in range(5):
    temp=str(input())
    a.append(temp)
    first.append(int(temp[-1]))
nin=0
nva=9

for i in range(5):
    if first[i]!=0 and first[i]<nva:
        nin=i
        nva=first[i]

ans=0
for i in range(5):
    if i!=nin:
        temmp=int(a[i])
        temmp=math.ceil((temmp-0.5)/10)*10
        ans+=temmp
    else:
        ans+=int(a[i])
print(ans)