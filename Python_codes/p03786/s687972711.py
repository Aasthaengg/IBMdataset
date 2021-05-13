N=int(input())
a=list(map(int,input().split()))
A=[]
for i in range(N):
    A.append([i,a[i]])
A.sort(key=lambda x:x[1])
sm=0
t=0
for i in range(N-1):
    sm+=A[i][1]
    if 2*sm<A[i+1][1]:
        t=i+1
print(N -t)