a,b,c=map(int,input().split())
x=0
for i in range(1,b+1):
    if i*a%b==c:
        x+=1
if x==0:
    print('NO')
else:
    print('YES')