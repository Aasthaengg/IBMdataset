import sys

line = sys.stdin.readline()
tate, yoko = line.split(" ")

S = int(tate) * int(yoko)
L = 2*int(tate) + 2*int(yoko)
print S, L