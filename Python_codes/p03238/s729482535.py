import sys
L = list()
for e in map(int, sys.stdin):
    L.append(e)
if len(L) == 1:
    print('Hello World')
else:
    print(L[1]+L[2])
