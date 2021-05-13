n = int(input())
a = [int(input()) for i in range(n)]

sign = a.index(max(a))
M = max(a)

a.remove(M)

S = max(a)

for i in range(n):
    if i != sign:
        print(M)
    else:
        print(S)
