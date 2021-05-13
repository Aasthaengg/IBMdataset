h=int(input())
x=0
while h>0:
    x+=1
    h//=2
ans=0
tmp=1
for i in range(x):
    ans+=tmp
    tmp*=2
print(ans)