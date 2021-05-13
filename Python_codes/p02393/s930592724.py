import sys

line = sys.stdin.readline()
inp = []
for i in line.split(" "):
    inp.append(int(i))

inp.sort()

print("%d %d %d" % (inp[0],inp[1],inp[2]))