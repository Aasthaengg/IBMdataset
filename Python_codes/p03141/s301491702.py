n=int(input())
AB=[list(map(int,input().split())) for _ in range(n)]

A,B=[],[]
for i,j in AB:
    A.append(i+j)
    B.append(-j)

ans=sum(B)
A=sorted(A)[::-1]
for i in range(0,n,2):
    ans +=A[i]

print(ans)