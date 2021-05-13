import sys
s=""
for line in sys.stdin:
    s+=line.lower()
alphabet=list("abcdefghijklmnopqrstuvwxyz")
for i in alphabet:
    print("{} : {}".format(i, s.count(i)))