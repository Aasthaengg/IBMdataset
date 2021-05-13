N,D=map(int,input().split())
count=0
n=0
for i in range(N):
    n=n+2*D+1
    if n>=N:
        print(i+1)
        break