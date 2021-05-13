a_b = raw_input().split(" ")
a = int(a_b[0])
b = int(a_b[1])
if a > b:
    print "a > b"
elif a < b:
    print "a < b"
else:
    print "a == b"