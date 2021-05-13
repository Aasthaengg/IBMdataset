import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
X = int(readline())
for a in range(-119,121):
    for b in range(-119,121):
        if (a**5-b**5) == X:
            print(a,b)
            sys.exit()