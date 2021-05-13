import sys

for i in sys.stdin:
    if int(i) == 0:
        break
    print(sum(map(int, i.rstrip())))