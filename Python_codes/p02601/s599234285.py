a,b,c=map(int,input().split())
k=int(input())

count=0
while a>=b:
    b*=2
    count+=1
while b>=c:
    c*=2
    count+=1
if count>k:
    print('No')
else:
    print('Yes')