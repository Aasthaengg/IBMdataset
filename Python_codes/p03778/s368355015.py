w,a,b=map(int,input().split())
x=min(a,b)
y=max(a,b)
print(y-x-w if y-x>w else 0)