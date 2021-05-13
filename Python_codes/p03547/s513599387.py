import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, y = readline().decode().split()
# x = int(x.lower(), 16)
# y = int(y.lower(), 16)
if x < y:
    print('<')
elif x == y:
    print('=')
else:
    print('>')
