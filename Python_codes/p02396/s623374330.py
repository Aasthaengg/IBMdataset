lis = []
a = raw_input()
while a != '0':
 lis.append(a)
 a = raw_input()

for i,v in enumerate(lis):
 print "Case %d: %s" % (i+1,v)