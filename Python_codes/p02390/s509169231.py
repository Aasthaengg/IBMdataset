n = input()
s = n % 60
m =((n % 3600) - s) / 60
h = n / 3600
print '%d:%d:%d' % (h, m, s)