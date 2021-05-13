A,B,C = map(int,input().split())
tmp = A
A = B
B = tmp
tmp = A
A = C
C = tmp
print(A,B,C)