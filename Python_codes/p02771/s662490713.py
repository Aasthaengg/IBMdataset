import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
A,B,C = map(int, readline().split())
if (A == B and B != C) or (B == C and C != A) or (A == C and C != B):
    print('Yes')
else:
    print('No')