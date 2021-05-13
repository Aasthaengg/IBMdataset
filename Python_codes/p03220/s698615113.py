N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))

x=[0]*N
for i in range(N):
    x[i]=abs(T-H[i]*0.006-A)


print(1+x.index(min(x)))
