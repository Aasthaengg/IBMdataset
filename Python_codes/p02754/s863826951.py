N, A, B = map(int , input().split())
 
L = []
i = 0
k = 0
j = 0
P = N // (A + B)
Q = N % (A + B)

if A > Q:
    print((P * A) + Q)
else:
    print((P * A) + A)
 