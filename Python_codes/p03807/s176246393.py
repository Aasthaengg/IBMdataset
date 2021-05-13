n=int(input())
l=list(map(int,input().split()))
ans1=0
ans2=0
for i in range(len(l)):
    if l[i]%2==0:
        ans2+=1
    if l[i]%2==1:
        ans1+=1
if  ans1%2==0:
    print('YES')
else:
    print('NO')