n,k=map(int,input().split())
a=[0]*n
b=[0]*k
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
b=a[:k]
print(sum(b))