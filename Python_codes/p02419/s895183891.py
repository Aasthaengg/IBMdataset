import sys
w = input()
c = 0
for line in sys.stdin:
    if line == "END_OF_TEXT\n":
        break
    T = line.lower().split()
    c += T.count(w)
print(c)