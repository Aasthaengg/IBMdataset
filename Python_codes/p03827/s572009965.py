import sys
N = int(input())
S = str(input())
if N <= 0 or N > 100:
    sys.exit()
x = 0
max = 0
for I in S:
    if I == "I":
        x += 1
        if max < x:
            max = x
        continue
    if I == "D":
        x -=1
        continue
print(max)