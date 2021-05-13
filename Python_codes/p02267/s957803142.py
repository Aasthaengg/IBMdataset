n = int(input())
S = [int(i) for i in input().split()] + [0]
q = int(input())
T = [int(i) for i in input().split()]
c = 0

for i in T:
    S[n] = i
    j = 0
    while i != S[j]:
        j += 1
    if j != n:
        c += 1

print(c)