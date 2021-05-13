import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

X = read().rstrip().decode()

s, t = 0, 0
for x in X:
    if x == 'S':
        s += 1
    else:
        if s == 0:
            t += 1
        else:
            s -= 1

print(s+t)