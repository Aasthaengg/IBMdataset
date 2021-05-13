lis = []
a = int(raw_input())
while a != 0:
 lis.append(a)
 a = int(raw_input())

for i,v in enumerate(lis):
 print "Case %d: %d" % (i+1,v)