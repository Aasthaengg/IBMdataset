a, b, c = map(int, input().split())
C = a + b
A = b + c
B = c + a

if a == A or b == B or C == c: print("Yes")
else: print("No")
