# Aizu Problem ITP_1_9_A: Finding a Word
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input2.txt", "rt")


word = input().strip().lower()
count = 0
while True:
    text = input().strip()
    if text == "END_OF_TEXT":
        break
    text = text.lower().split()
    count += text.count(word)
print(count)