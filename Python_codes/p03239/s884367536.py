N,T=map(int,input().split())
a=10000
for i in range(N):
    c,t=map(int,input().split())
    if t<=T and c<a:a=c
print(a if a!=10000 else 'TLE')