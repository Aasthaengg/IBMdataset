[a,b] = raw_input().split()
a = int(a)
b = int(b)
print "%d %d %0.5f" % (a / b, a % b, float(a) / float(b))