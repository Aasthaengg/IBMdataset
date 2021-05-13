import sys

def seiseki(m, f, r):
    if m == -1 or f == -1:
        return "F"
    elif m + f >= 80:
        return "A"
    elif 65 <= m + f < 80:
        return "B"
    elif 50 <= m + f < 65:
        return "C"
    elif 30 <= m + f < 50:
        if r >= 50:
            return "C"
        return "D"
    elif m + f < 30:
        return "F"

for line in sys.stdin:
    m, f, r = map(int, line.strip().split())
    if m == f == r == -1:
        break

    print seiseki(m, f, r)