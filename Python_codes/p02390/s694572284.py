sa = raw_input()
sa = int(sa)

s = sa % 60
ma = sa / 60
m = ma % 60
h = ma / 60

print ('%d:%d:%d') % (h,m,s)