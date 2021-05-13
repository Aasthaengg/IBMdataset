n,k=map(int,input().split())
lh=list(map(int,input().split()))
la=[i for i in lh if i>=k]
print(len(la))