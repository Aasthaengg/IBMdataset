a = int(input())
h = a//3600
a = a - (3600*h)
m = a//60
a = a - (60*m)
h = str(h)
m = str(m)
a = str(a)
time = h+':'+m+':'+a
print(time)