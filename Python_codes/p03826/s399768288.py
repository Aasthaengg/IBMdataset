a,b,c,d=map(int,input().split())
print(max(a*b,c*d) if a*b!=c*d else a*b)