a, b = map(int, input().split())
x,y=divmod(a,b)
print(x,y,"{0:.8f}".format(round(a/b, 8)))