from sys import stdin

x, a = (int(x) for x in stdin.readline().rstrip().split())
print(0 if x<a else 10)