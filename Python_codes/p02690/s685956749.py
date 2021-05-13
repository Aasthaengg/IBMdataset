import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x = int(readline())

for a in range(-140, 140):
    for b in range(-140, 140):
        if a ** 5 - b ** 5 == x:
            print(a, b)
            exit()
