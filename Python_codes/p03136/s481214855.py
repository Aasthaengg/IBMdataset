n=int(input())
s=list(map(int,input().split()))
x=max(s)
y=sum(s)
       
if y>2*x:
       print('Yes')
else:
       print('No')