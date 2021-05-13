#n=int(input())
a,b=map(str,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
n=int(a+b)
flag='No'
for i in range(1,n+1):
    if i*i==n:
        flag='Yes'
print(flag)