import sys

s = str()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for line in sys.stdin:
    s += line.lower()

for c in alphabet:
    print(c+" : "+str(s.count(c)))