N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
num=0
for i in range(N):
    if i==0:
        num=(T-H[0]*0.006)
        spot=0
    else:
        if abs(A-(T-H[i]*0.006))<=abs(A-num):
            num=(T-H[i]*0.006)
            spot=i

print(spot+1)
