import sys
N=int(input())
A=[[*map(int,ln.split())] for ln in sys.stdin]

ans=0
a=0
for i in range(N):
    a+=A[0][i]
    b=a
    for j in range(i,N):
        b+=A[1][j]
    ans=max(ans,b)

#print(A)
print(ans)
