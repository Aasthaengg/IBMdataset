S =input()
h = int(int(S / 60) / 60)
m = int(S/60) % 60
s = S % (60*60) % 60
print "%d:%d:%d" % (h, m, s)