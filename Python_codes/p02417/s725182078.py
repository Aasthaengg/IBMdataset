# Aizu Problem ITP_1_8_C: Counting Characters
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


letters = [chr(k) for k in range(97, 123)]
count = {char: 0 for char in letters}
for line in sys.stdin:
    for char in line.lower():
        if char in letters:
            count[char] += 1

for char in letters:
    print(char, ':', count[char])