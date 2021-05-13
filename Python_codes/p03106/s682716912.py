import sys
A,B,K = map(int,input().split())
#euclid algorithm
if A < B: 
    A, B = B, A
while A%B != 0:
    A,B = B,A%B

count = 0
for I in range(B,0,-1):
    if B % I == 0:
        count += 1
    if count == K:
        print(I)
        break
