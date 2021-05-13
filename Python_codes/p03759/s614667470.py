i = [int(s) for s in input().split()]
A = i[1] - i[0]
Atwo = i[2] - i[1]
if A == Atwo:
    print("YES")
else:
    print("NO")
