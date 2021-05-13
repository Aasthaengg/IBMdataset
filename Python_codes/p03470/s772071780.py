N = int ( input ())
l = []
for i in range (N):
    a = int ( input ())
    l.append (a)
l = list(set(l))
print (len (l))