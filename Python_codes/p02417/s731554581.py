import sys

s = []
for line in sys.stdin:
    s.extend(list(line.lower()))  

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    print(i + " : " + str(s.count(i)))