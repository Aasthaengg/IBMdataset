a,b,c=list(map(int,input().split()))
flag=0
for itr in range(1,100000):
    if (a*itr)%b==c: 
        print('YES')
        flag=1
        break
if flag==0: print('NO')