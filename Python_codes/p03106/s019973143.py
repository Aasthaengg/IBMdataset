import sys
A,B,K = map(int,input().split())
if not ( 1 <= A <= 100 and 1 <= B <= 100 ): sys.exit()
if not ( 1 <= K ): sys.exit()
#euclid algorithm
if A < B: 
    A, B = B, A
while A%B != 0:
    A,B = B,A%B
# B is greatest common divisor
count = 0
for I in range(B,0,-1):
    if B % I == 0:
        count += 1
    if count == K:
        print(I)
        break
