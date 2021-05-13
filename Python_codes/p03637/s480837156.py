N=int(input())
a=list(map(int,input().split()))
b4=[x for x in a if x%4==0]
a4=[x for x in a if x%4!=0]
b2=[x for x in a4 if x%2==0]
c=[x for x in a4 if x%2!=0]
if len(b4)==0 and (len(c)==0 and len(b2)>1):
    print('Yes')
elif len(b4)==0 and len(c)!=0:
    print('No')
elif len(b4)+1<len(c):
    print('No')
elif len(b4)<len(c) and len(b2)>0:
    print('No')
else:
    print('Yes')