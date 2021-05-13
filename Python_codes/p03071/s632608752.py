a,b = map(int,input().split())
print ((max(a,b)*2)-1) if 1 <= abs(a-b) else print (a*2)
