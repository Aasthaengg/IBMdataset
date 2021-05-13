N=int(input())
A=[int(input()) for _ in range(N)]

B=sorted(A)

for n in range(N):
    if A[n]!=B[-1]:
        print(B[-1])
    else:
        print(B[-2])