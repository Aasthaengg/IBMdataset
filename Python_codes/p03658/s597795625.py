n,k=map(int,input().split())
l=list(map(int,input().split()))

l2=sorted(l, reverse=True)
length = sum(l2[0:k])
print(length)