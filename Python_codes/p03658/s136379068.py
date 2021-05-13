N,K=map(int,input().split())
arg=list(map(int,input().split()))
arg=sorted(arg,reverse=True)
ans=0
print(sum(arg[0:K]))