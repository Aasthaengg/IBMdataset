import sys

#fin = open("test.txt", "r")
fin = sys.stdin

str = fin.readline()

print(str.swapcase(), end="")