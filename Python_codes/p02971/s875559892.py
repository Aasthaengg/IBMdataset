N = int(input())
A = [int(input()) for _ in range(N)]
B=sorted(A)
C=max(A)
for i in A:
    if C==i:
        print(B[-2])
    else:
        print(C)