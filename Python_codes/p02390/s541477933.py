#usr/bin/python

S = raw_input()

h = int(S) / 3600
m = int(S) % 3600 / 60
s = int(S) % 3600 % 60 

print  "%s:%s:%s" % (h, m, s)