import sys

line = sys.stdin.readline()
inp = []
for i in line.split(" "):
    inp.append(int(i))
print (inp[0]*inp[1], (inp[0]+inp[1])*2)