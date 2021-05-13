N=int(input())
A=[int(input()) for _ in range(N)]
s=sorted(A)
for a in A:
    print(s[-1] if a!=s[-1] else s[-2])