# ABC 097: A – Colorful Transceivers
a, b, c, d = [int(s) for s in input().split()]
print('Yes' if abs(c - a) <= d or (abs(b -a) <= d and abs(c - b) <=d) else 'No')