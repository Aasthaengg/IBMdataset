from sys import stdin
n,h,w = [int(x) for x in stdin.readline().rstrip().split()]
data = [stdin.readline().rstrip().split() for _ in range(n)]
o=0
for rect in data:
    if int(rect[0])>=h and int(rect[1])>=w:
        o+=1

print(o)