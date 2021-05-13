from sys import stdin
X,t = [int(x) for x in stdin.readline().rstrip().split()]
print(max(0,X-t))