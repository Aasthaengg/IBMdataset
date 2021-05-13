from sys import stdin

a,b,c = [int(x) for x in stdin.readline().rstrip().split()]

point = 0

if a+b >= c:
    point += c
else:
    point += a+b+1

point += b

print(point)