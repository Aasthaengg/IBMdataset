a,b,c,d=map(int,input().split())
ans=0
if abs(a-c)<=d:
    ans+=1
elif abs(a-b)<=d and abs(b-c)<=d:
    ans+=1
else:
    ans+=0
if ans>=1:
    print('Yes')
else:
    print('No')