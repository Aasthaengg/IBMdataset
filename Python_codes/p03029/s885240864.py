from sys import stdin

a, p = (int(x) for x in stdin.readline().rstrip().split())
print(((3*a)+p)//2)
