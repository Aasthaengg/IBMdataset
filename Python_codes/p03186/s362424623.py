import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A,B,C = map(int,read().split())

answer = 0
# C,B,C,B,...
x = min(B,C)
answer += x + x
B -= x
C -= x
if B:
    answer += B
else:
    # C,A,C,A,
    x = min(C,A+1)
    answer += x
print(answer)