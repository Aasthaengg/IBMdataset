ans=[0]*4

for i in range(3):
    a,b=map(int,input().split())
    ans[a-1]+=1
    ans[b-1]+=1

f1=0
f2=0
for i in range(4):
    if ans[i]==1:
        f1+=1
    if ans[i]==2:
        f2+=1
if f1==2 and f2==2:
    print('YES')
else:
    print('NO')