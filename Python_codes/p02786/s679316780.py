import os, sys
if os.environ.get("DEBUG") is not None:
    sys.stdin = open("in.txt", "r")
rl = sys.stdin.readline

h = int(rl())
i = 1
while True:
    if h <= 2**i - 1:
        print(2**i - 1)
        break
    i += 1
