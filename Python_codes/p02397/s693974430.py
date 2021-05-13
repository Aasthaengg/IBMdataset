import sys

for line in sys.stdin:
    [a, b] = [int(x) for x in line.split()]

    if [a, b] == [0, 0]:
        break

    if b < a:
        print(" ".join([str(x) for x in [b, a]]))
    else:
        print(" ".join([str(x) for x in [a, b]]))