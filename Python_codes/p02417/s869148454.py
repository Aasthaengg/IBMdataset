import sys

inp = sys.stdin
counter = {}

for text in inp:
    for a in text:
        a = a.lower()
        counter[a] = counter.get(a,0) + 1

for x in range(26):
    a = chr(ord('a')+x)
    print("{0} : {1}".format(a,counter.get(a,0)),sep='')
