N = int(input())
c = list(input())
w = c.count("W")
r = c.count("R")
wr = c[len(c) - w:].count("W")

print(min(r, w - wr))
