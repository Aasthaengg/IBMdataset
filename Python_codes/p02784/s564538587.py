H,N=map(int,input().split())
A=list(map(int,input().split()))
a=0
for i in A:
    a+=i
if a>=H:
    print('Yes')
else:
    print('No')