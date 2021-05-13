s = input()
hour = 3600
minite = 60
h = 0
m = 0

h = s / hour
m = (s - h * hour) / minite
s  = s - h * hour - m * minite

print "%d:%d:%d" %(h, m, s)