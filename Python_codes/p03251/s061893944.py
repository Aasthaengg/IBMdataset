n,m,X,Y = map(int,input().split())
x = sorted(map(int,input().split())) + [X]
y = sorted(map(int,input().split())) + [Y]
print("No War" if max(x) < min(y) else "War")