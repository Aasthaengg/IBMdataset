# Python 3+
import sys

#file = open("test.txt")
file = sys.stdin

data = list( map(int, file.readline().split()) )

if data[0] > data[2] :
    data[2],data[0] = data[0],data[2]

if data[0] > data[1] :
    data[1], data[0] = data[0], data[1]

if data[1] > data[2] :
    data[2],data[1] = data[1], data[2]

out = " ".join(map(str, data))
print(out)