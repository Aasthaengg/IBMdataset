# Aizu Problem ITP_1_9_D: Transformation
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input2.txt", "rt")


string = [_ for _ in input().strip()]
n = int(input())
for _ in range(n):
    s = input().split()
    a, b = int(s[1]), int(s[2])
    cmd = s[0]
    if cmd == "print":
        print(''.join(string[a:b+1]))
    elif cmd == "reverse":
        tmp = string[a:b+1]
        string[a:b+1] = [_ for _ in tmp[::-1]]
    elif cmd == "replace":
        for p in range(a, b + 1):
            string[p] = s[3][p-a]