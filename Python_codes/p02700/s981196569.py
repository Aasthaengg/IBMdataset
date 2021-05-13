A, B, C, D = map(int, input().split())

t = 1
while (A > 0) and (C > 0):
    if t > 0:
        C -= B
    else:
        A -= D
    t = (t + 1) % 2

if C <= 0:
    print("Yes")
else:
    print("No")