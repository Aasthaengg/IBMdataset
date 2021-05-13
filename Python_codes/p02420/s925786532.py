# Aizu Problem ITP_1_9_B: Shuffle
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


while True:
    string = input().strip()
    if string == '-':
        break
    n = int(input())
    for _ in range(n):
        h = int(input())
        string = string[h:] + string[:h]
    print(string)