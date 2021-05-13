#n=int(input())
#a,b=map(int,input().split())
l1=list(input())
l2=list(input())
#l=[list(map(int,input().split())) for i in range(2)]
if l1 == l2[::-1]:
    print('YES')
else:
    print('NO')