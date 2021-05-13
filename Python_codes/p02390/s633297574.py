t = int(raw_input())
h = t / (60*60)
t = t - h * 60 * 60
s = t / 60
t = t - s * 60
print "%d:%d:%d" % (h,s,t)