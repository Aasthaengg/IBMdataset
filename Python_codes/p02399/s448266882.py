a,b = (int(i) for i in input().split())
d = int(a/b)
r = int(a%b)
print(str(d)+" "+str(r),end=" ")
print("%.5f" % (a/b))