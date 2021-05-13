S = input()

m = S/60
s = S%60

h = m/60
m = m%60

print "%d:%d:%d" % (h,m,s)