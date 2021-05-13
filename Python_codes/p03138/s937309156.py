from collections import defaultdict
x,y=map(int,input().split())
a=list(map(int,input().split()))
lol=[]
for i in a:
    b=bin(i)[2:]
    lol.append("0"*(40-len(b))+b)
d=defaultdict(int)
for i in lol:
    for j in range(1,41):
        if i[-j]=="1":
            d[j]+=1
        else:
            d[j]-=1
            
s=""      
p=0
for i in range(1,41):
    if d[41-i]<0 and p+2**(40-i)<=y:
        s+="1"
        p+=2**(40-i)
    else:
        s+="0"
s=int(s,2)
k=0
for i in a:
    k+=i^s
print(k)    