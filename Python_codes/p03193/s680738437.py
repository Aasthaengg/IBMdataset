n,h,w=map(int,input().split())
print(n-sum(a<h or b<w for a,b in [list(map(int,input().split())) for i in range(n)]))
