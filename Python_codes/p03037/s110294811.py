n,m = map(int,input().split())
k = [list(map(int,input().split())) for i in range(m)]
l,r = [list(i) for i in zip(*k)]
x = max(l)
y = min(r)
print(max(y-x+1,0))