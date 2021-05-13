import sys
import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
a,b = readline().rstrip().decode('utf-8').split()

if a == "H":
    print(b)
else:
    if b == "H":
        print("D")
    else:
        print("H")