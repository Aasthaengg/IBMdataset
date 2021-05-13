x = int(input())
sec = x%60
y = x/60
min = y%60
hrs = y/60

print str(hrs)+":"+str(min)+":"+str(sec)