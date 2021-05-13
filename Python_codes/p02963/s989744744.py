import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = int(read())

A = 10 ** 9; B = 1
D = (S + (-S) % A) // A
C = (A * D - S) // B

print(0,0,A,B,C,D)