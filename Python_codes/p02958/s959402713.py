N=int(input())
p=list(map(int,input().split()))
alis=[i for i  in range(1,N+1)]

newlist=[x-y for (x,y) in zip (p,alis)]


if sum(1 for x in newlist if x!=0)==2 or sum(1 for x in newlist if x!=0)==0 :
    print('YES')
else:
    print('NO')

