import sys

n = int(input())
s = input()

l = 0
r = n
while l < n and s[l] == ".":
    l += 1
while r > 0 and s[r-1] == "#":
    r -= 1
if l >= r:
    print(0)
    sys.exit()

A = []
a = 0
b = 0
for i in range(l, r):
    if s[i] == "#":
        if b > 0:
            A.append([a, b])
            a = 1
            b = 0
        else:
            a += 1
    else:
        b += 1
if b > 0:
    A.append([a, b])
# print(A)

DP = [0, 0]
for i in range(len(A)):
    DPN = DP[:]
    DPN[0] = min(DP) + A[i][1]
    DPN[1] = DP[1] + A[i][0]
    DP = DPN[:]
print(min(DP))