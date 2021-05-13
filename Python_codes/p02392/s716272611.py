import sys

line = sys.stdin.readline()
inp = []
for i in line.split(" "):
    inp.append(int(i))

if inp[0]>=inp[1]:
    print("No")
elif inp[1]>=inp[2]:
    print("No")
else:
    print("Yes")