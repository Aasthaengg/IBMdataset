[P,Q,R] = list(map(int,input().split()))

A = P + Q
B = Q + R
C = R + P

print(min(A,B,C))