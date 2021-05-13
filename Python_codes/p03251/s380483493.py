N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
print ("No War") if max(x) < min(y) and (X < max(x) < Y or X < min(y) <= Y) else print ("War")
