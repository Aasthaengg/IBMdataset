s_sum = input()
h = s_sum / 3600
m = (s_sum - 3600*h) / 60
s = s_sum - 3600*h - 60*m

print '%d:%d:%d' % (h,m,s)