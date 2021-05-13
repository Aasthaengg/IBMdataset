f=lambda:map(int,input().split())
n,T=f()
m=min([1001]+[c for c,t in [f() for _ in range(n)] if t<=T])
print([m,'TLE'][m>1000])