import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, k = [int(readline()) for _ in range(2)]
x = [min(abs(int(x)-0), abs(int(x)-k))*2 for x in readline().split()]
print(sum(x))