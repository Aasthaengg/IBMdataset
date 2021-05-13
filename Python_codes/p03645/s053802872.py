n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(m)]
f=set([ft[1] for ft in ab if ft[0]==1])
t=set([ft[0] for ft in ab if ft[1]==n])
if f&t: print("POSSIBLE")
else: print("IMPOSSIBLE")