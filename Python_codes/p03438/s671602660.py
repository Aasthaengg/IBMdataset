N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

v = 0
for a, b in zip(A, B):
    if b - a > 0:
        v += (b - a) // 2
    else:
        v += b - a
if v >= 0:
    print("Yes")
else:
    print("No")
