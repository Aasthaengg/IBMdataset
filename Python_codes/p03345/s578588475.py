
A, B, C, K = map(int, input().split())

AA = B+C
BB = A+C
CC = A+B

if K%2==0:
    print(A-B)
else:
    print(AA-BB)