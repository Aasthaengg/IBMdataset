in_str = raw_input().split()
a = int(in_str[0])
b = int(in_str[1])
print "a",
if(a<b):
    print "<",
elif(a>b):
    print ">",
else:
    print "==",
print "b"