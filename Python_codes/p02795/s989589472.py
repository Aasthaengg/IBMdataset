from sys import stdin
H = int(stdin.readline().rstrip())
W = int(stdin.readline().rstrip())
N = int(stdin.readline().rstrip())
print((N-1)//max(H, W) + 1)