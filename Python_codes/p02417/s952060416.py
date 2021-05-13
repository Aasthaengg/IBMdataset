import sys

a = ""
for input in sys.stdin:
    a += input.lower()
for i in range(97,123):
    print "%c : %d"%(chr(i),a.count(chr(i)))
