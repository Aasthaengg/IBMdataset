def getint():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

x,a = getint()
if x >= a:
    print(10)
else:
    print(0)