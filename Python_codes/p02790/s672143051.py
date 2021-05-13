a,b = map(int,input().split())

v=0
for i in range(max(a,b)):
    v = v*10+min(a,b)    

print( v )