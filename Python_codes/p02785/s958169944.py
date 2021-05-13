N,K=map(int,input().split())
H=list(map(int,input().split()))
newlist=sorted(H,reverse=True)
del newlist[0:K]
print(sum(newlist))