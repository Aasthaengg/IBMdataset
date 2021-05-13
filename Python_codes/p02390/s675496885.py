x = int(raw_input())

s = x % 60
m = x // 60 % 60
h = (x // 60) // 60

print str(h) + ":" + str(m) + ":" + str(s)