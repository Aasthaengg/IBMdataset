N=int(input())
A=[int(input()) for _ in range(N)]
B=sorted(A)[:N-1]
m=max(A)
n=A.index(max(A))
for i in range(N):
    if  i!=n:
        print(m)
    else:
        print(max(B))