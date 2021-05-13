n,a,b=map(int,input().split())
print(a if a<b else b, 0 if a+b<n else a+b-n)