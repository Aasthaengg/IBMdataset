from __future__ import print_function
n = int(raw_input())

for i in range(n+1):
    if i != 0 and i % 3 == 0:
        print (" %i" % i, end="")
    elif i != 0 and i % 10 == 3:
        print (" %i" % i, end="")
    else:
        if str(i).find('3') >= 0:
            print (" %i" % i, end="")
print("")