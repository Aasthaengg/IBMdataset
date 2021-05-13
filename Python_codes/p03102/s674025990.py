f=lambda:[*map(int,input().split())]
n,m,c=f()
l=f()
print(sum(sum(a*b for a,b in zip(f(),l))>-c for _ in range(n)))