N,M=map(int,input().split())
hen=[0 for i in range(0,N-1)]
for i in range(0,M):
    a,b=map(int,input().split())
    if a==1:
        hen[b-2]+=1
    elif b==1:
        hen[a-2]+=1
    else:
        hen[a-2]+=1
        hen[b-2]+=1

flag=0
for i in range(0,N-1):
    if hen[i]%2==1:
        flag=1

if flag==0:
    print('YES')
else:
    print('NO')
