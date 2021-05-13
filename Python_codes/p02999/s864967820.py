import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

X,A = map(int,read().split())
answer = 0 if X < A else 10
print(answer)