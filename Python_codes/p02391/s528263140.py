# Python 3+
import sys

#file = open("test.txt")
file = sys.stdin

a, b = map(int, file.readline().split())

if a < b :
    output = "a < b"
elif a > b :
    output = "a > b"
else :
    output = "a == b"

print(output)