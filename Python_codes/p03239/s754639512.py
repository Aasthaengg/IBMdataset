n,t=map(int,input().split())
d={i:j for i,j in [list(map(int,input().split())) for _ in range(n)] if j<=t}
print(sorted(d.items(),key=lambda x:x[0])[0][0] if d else'TLE')