# Aizu Problem ITP_1_8_A: Toggling Cases
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


out = ""
for char in input().strip():
    o = ord(char)
    if 65 <= o <= 90:
        out += chr(o + 32)
    elif 97 <= o <= 122:
        out += chr(o - 32)
    else:
        out += char
print(out)