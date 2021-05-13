n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
a=[list(map(int,input().split())) for i in range(2)]
mx=0
for i in range(n):
    mx=max(mx,sum(a[0][0:i+1])+sum(a[1][i:n]))

print(mx)

