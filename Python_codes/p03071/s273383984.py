a,b=map(int,input().split())
M=max(a,b)
m=min(a,b)

n=0
n+=M
M-=1

n+=max(M,m)

print(n)