n = int(input())
A,B = map(int,input().split())
for _ in range(n-1):
    a,b = map(int,input().split())
    aa = 0
    bb = 0
    if A % a == 0:
        aa = A // a
    else:
        aa = A // a + 1
    if B % b == 0:
        bb = B // b
    else:
        bb = B // b + 1
    m = max(aa, bb)
    A,B = a * m, b * m
print(A+B)