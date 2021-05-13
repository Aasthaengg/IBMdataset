
sec = int(input())

m = sec//60
sec %= 60
h = m//60
m%=60
print("{}:{}:{}".format(h,m,sec))
