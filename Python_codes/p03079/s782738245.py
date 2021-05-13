a,b,c=map(int,input().split())
print("YNeos"[a!=b or b!=c or c!=a::2])
