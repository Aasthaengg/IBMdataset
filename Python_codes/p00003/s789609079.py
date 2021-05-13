import sys
l = sys.stdin.readlines ()
del l[0] # Delete number represents the number of detasets.
for line in l:
    data = map (int, line.split (" "))
    data.sort(reverse=True)
    if data[0]**2 == data[1]**2 + data[2]**2:
        print ("YES")
    else: print ("NO")