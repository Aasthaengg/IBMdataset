n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if min(a,b,c,d,e)==1:
    print(n//(min(a,b,c,d,e))+4)
else:
    print(n//(min(a,b,c,d,e))+5)