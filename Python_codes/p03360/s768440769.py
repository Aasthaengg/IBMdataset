#n=int(input())
a,b,c=map(int,input().split())
k=int(input())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

mx=max(a,b,c)
total=a+b+c-mx
for i in range(k):
    mx=2*mx

print(total+mx)
