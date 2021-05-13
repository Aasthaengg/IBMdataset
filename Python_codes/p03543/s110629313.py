#n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
n=list(input())
if len(set(n[0:3])) == 1 or len(set(n[1:])) == 1 :
    print('Yes')
else:
    print('No')