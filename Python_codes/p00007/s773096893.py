import sys

n = int(sys.stdin.readline())
borrowing = 100000

for i in range(0, n):
    borrowing *= 1.05
    borrowing = int((borrowing+999) / 1000) * 1000

print(borrowing)