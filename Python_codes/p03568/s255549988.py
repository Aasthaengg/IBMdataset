import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

e = 0
for a in A:
    if a % 2 == 0:
        e += 1 

print(3 ** N - 2 ** e)
