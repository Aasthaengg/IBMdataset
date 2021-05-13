from sys import stdin

n = stdin.readline().rstrip()
a = [int(x) for x in stdin.readline().rstrip().split()]

minc = 10**9

for b in a:
    count = 0
    while True:
        if b % 2 == 1: break
        b = b//2
        count = count + 1

    minc = min([minc, count])

print(minc)