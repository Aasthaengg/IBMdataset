from collections import Counter
H,W=map(int,input().split())
li=[]
for i in range(H):
    a=list(input())
    li+=a
c=Counter(li)
t,o=0,0
for x,y in c.items():
    l=y%4
    t+=l//2
    o+=l%2
isok=True
if(H%2==0 and W%2==0):
    if t!=0 or o!=0:
        isok=False
elif(H%2==0 and W%2==1):
    if(t>H//2 or o>0):
        isok=False
elif(H%2==1 and W%2==0):
    if(t>W//2 or o>0):
        isok=False
else:
    if(t>W//2+H//2 or o>1):
        isok=False
print('Yes' if isok else 'No')