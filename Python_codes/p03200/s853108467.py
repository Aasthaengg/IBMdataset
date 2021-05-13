import sys
a = [ c for c in input()]
B = 0
W = 0
for i in range(len(a)):
    if a[i] == "B":
        B += 1
    else:
        W += B

print(W)