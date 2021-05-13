def connect(s,t,u):
    return abs(s-t)<=u
a,b,c,d=map(int,input().split())
print("Yes" if connect(a,c,d) or connect(a,b,d) and connect(b,c,d) else "No")
