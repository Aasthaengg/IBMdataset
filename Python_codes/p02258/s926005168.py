n = input()
minSeq = input()
maxv = -float("inf")
for i in range(n-1):
    R = input()
    if R - minSeq > maxv:
        maxv = R - minSeq
    if R < minSeq:
        minSeq = R
print(maxv)