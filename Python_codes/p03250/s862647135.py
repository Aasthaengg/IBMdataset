import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = sorted(map(int, readline().split()), reverse=True)
print(n[0]*10+n[1]+n[2])
