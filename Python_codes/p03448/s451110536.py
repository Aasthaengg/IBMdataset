import sys
A = int(input())
B = int(input())
C = int(input())
X = int(input())

if not (0 <= A <= 50 and 0 <= B <= 50 and 0 <= C <= 50):
    sys.exit()
if not ( 1 <= A + B + C ):
    sys.exit()
if not ( 50 <= X <= 20000 ):
    sys.exit()
if X % 50 != 0:
    sys.exit()

count = 0
for I in range(A+1):
    for J in range(B+1):
        for K in range(C+1):
            if I * 500 + J * 100 + K * 50 == X:
                count += 1
print(count)