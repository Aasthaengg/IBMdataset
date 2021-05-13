i = raw_input().strip().split()
 
a = int(i[0])
b = int(i[1])
 
if a < b:
    print "a < b"
elif a > b:
    print "a > b"
elif a == b:
    print "a == b"