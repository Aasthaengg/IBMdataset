N=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))
B=[V[i]-C[i] for i in range(N)]
ans=sum([B[i] for i in range(N) if B[i]>0])
print(ans)