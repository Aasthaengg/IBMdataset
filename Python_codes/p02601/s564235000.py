a,b,c=[int(i) for i in input().split()]
n=int(input())
flag=0
e=0
while(a>=b):
    b=b*2
    e=e+1
while(e<n and c<=b):
    c=c*2
    e=e+1
if(b>a and c>b and e<=n):
    print('Yes')
else:
    print('No')