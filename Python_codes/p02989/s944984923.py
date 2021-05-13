N=int(input())
D=list(map(int,input().split()))
D.sort()

S=D[N//2]-D[N//2-1]
if S>=0:
    print(S)
else:
    print(0)
