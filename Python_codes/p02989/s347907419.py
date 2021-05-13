N=int(input())
*D,=map(int,input().split())

for i in range(N):
    D[i]=(D[i],i)
D=sorted(D)
print(D[N//2][0]-D[N//2-1][0])