n=int(input())
l=list(map(int,input().split()))
d=[]
s=[]
for i in range(n):
    if(i%2==0):
        d.append(l[i])
    else:
        s.append(l[i])
if(n%2==0):
    s.reverse()
    print(*(s+d))
else:
    d.reverse()
    print(*(d+s))
