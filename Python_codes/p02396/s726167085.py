import sys
#a = open("test.txt", "r")
a = sys.stdin
 
count = 1
for line in a:
    if int(line) == 0:
    	break
    print("Case {0}: {1}".format(count, line), end="")
    count = count + 1