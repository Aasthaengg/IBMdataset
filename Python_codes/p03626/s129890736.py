n=int(input())
s1=input()
s2=input()
x=[]
f=0
for i in range(n):
    if f==1:
        f=0
    else:
        if s1[i]==s2[i]:
            x.append(0)
        else:
            x.append(1)
            f=1
l=len(x)
#print(x)
if l==1:
    if x[0]==0:
        print(3)
    else:
        print(6)
else:
    if x[0]==0:
        c=3
    else:
        c=6
    for i in range(1,l):
        #print(c)
        if x[i-1]==0:
            c*=2
        else:
            if x[i]==1:
                c*=3
        c%=1000000007

    print(c%1000000007)
