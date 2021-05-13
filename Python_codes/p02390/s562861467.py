
s = int(input())

h = int(s/3600)

m = int( (s - 3600*h)/60 )

d = s - 3600*h-60*m


print("{0}:{1}:{2}".format(h,m,d))
