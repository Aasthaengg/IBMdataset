# Aizu Problem ITP_1_8_D: Ring
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input2.txt", "rt")


def ring(string, pattern):
    string = string + string
    return string.find(pattern) >= 0

  
string = input().strip()
pattern = input().strip()
print("Yes" if ring(string, pattern) else "No")