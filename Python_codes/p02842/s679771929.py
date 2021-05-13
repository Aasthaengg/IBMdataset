n = int(input())
x = int((100*n)/108)
if n == int(x*1.08):
    print(x)
elif n == int((x+1)*1.08):
    print (x+1)
elif n == int((x-1)*1.08):
    print (x-1)
else:
    print(":(")