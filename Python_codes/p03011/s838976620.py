a,b,c = map(int,input().split())

l = min([a+b,b+c,c+a])
print(l)