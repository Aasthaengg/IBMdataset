n,k=map(int,input().split())
a=list(map(int, input().split()))
b=sorted(a,reverse=True)
print(sum(b[:k]))