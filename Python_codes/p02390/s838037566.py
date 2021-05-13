S = input()
h = S / (60*60)
m = (S - (h*60*60)) / 60
s = (S - (h*60*60) - (m*60))
print "%d:%d:%d" % (h,m,s)