n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
s=sum(l[k:])
print(s)
