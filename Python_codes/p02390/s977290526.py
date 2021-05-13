t = input()
h = int(t / 60**2)
m = int(t / 60) - h * 60
s = t -(h * 60**2 + m * 60) 
print str(h)+":"+str(m)+":"+str(s)