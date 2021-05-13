x = input()

h = x/3600
m = (x%3600)/60
s = x - (h*3600+m*60)

print "%d:%d:%d" % (h,m,s)