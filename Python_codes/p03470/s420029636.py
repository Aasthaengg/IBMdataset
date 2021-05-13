from sys import stdin

n = int(stdin.readline().rstrip())
d = []
for i in range(n):
    d.append(int(stdin.readline().rstrip()))

print (len(set(d)))






