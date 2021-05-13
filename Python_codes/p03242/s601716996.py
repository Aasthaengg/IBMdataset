import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = readline().decode().rstrip()

n = n.replace('1', 't').replace('9', '1').replace('t', '9')
print(int(n))
