# Python 3+
#-------------------------------------------------------------------------------
import sys

#ff = open("test.txt", "r")
ff = sys.stdin

while True :
    a, b = map(int, ff.readline().split())
    if (a == 0) & (b == 0) :
        break

    if a < b : print(a, b)
    else : print(b, a)

exit()