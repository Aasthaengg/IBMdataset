target = int(input())

m,s = divmod(target,60)
if m == 0:
    print("0:0:%d" % s)
else:
    h, m = divmod(m,60)
    print("%d:%d:%d" % (h,m,s))