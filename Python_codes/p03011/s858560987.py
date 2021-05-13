a,b,c = [int(a) for a in input().split()]
d = min(a+b,b+c,c+a)
print (d)