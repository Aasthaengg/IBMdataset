n,a,b = map(int,input().split(' '))
print("{0} {1}".format(min(a,b),max(a + b - n,0)))
