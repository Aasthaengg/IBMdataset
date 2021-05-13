number = raw_input().split(" ")
a = int(number[0])
b = int(number[1])
c = int(number[2])
if a < b < c:
    print "Yes"
else:
    print "No"