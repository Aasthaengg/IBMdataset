a = list(map(int, input().split()))
A = a[0]
B = a[1]
C = a[2]
D = a[3]

while A>0 and C>0:
    C = C - B
    if C <= 0:
        print("Yes")
        break
    A = A - D
    if A <= 0:
        print("No")