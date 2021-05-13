a,b,c,k=map(int,input().split())
inf=10**18+1

if k%2==0:
    ans=a-b
else:
    ans=b-a

if ans<inf:
    print(ans)
else:
    print('Unfair')