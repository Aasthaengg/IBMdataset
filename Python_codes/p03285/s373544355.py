n=int(input())
x=n//4
y=n//7
c=0
for i in range(x+1):
    for j in range(y+1):
        if 4*i+7*j==n:
            c+=1
            
if c>0:
    print('Yes')
else:
    print('No')