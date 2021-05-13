#good grid
n,c=map(int,input().split())
mod1=[]
mod2=[]
mod3=[]
change=[0 for j in range(c)]
for i in range(c):
    change[i]=list(map(int,input().split()))
    
for i in range(n):
    s=list(map(int,input().split()))
    for some in range(n):
        if (((some+1)+(i+1))%3)==0:
            mod3.append(s[some])
        if (((some+1)+(i+1))%3)==1:
            mod1.append(s[some])
        if (((some+1)+(i+1))%3)==2:
            mod2.append(s[some])
change_to_some=[[0 for i in range(c)]  for k in range(3)]
for j in range(c):
    a=0
    for k in (mod1):
        a+=change[k-1][j]
    change_to_some[0][j]=a
for j in range(c):
    a=0
    for k in (mod2):
        a+=change[k-1][j]
    change_to_some[1][j]=a
for j in range(c):
    a=0
    for k in (mod3):
        a+=change[k-1][j]
    change_to_some[2][j]=a

anslist=[]
for a in range(c):
    for b in range(c):
        for k in range(c):
            if a!=b and b!=k and a!=k:
                anslist.append(change_to_some[0][a]+change_to_some[1][b]+change_to_some[2][k])
print(min(anslist))