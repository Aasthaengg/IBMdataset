T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
A1 *= T1
A2 *= T2
B1 *= T1
B2 *= T2
if A1 > B1:
    A1, B1 = B1, A1
    A2, B2 = B2, A2
C = B1 - A1
D = A2 - B2

if C == D:
    print("infinity")
elif C > D:
    print(0)
else:
    q, r = divmod(C, (D - C))
    if r == 0:
        print(2 * q)
    else:
        print(2 * q + 1)