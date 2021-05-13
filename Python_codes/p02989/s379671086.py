N=int(input())
D=list(map(int,input().split()))
D=sorted(D)
l=D[N//2-1]
r=D[N//2]
print(r-l)