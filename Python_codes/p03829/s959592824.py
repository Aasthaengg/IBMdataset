N,A,B=map(int,input().split())
X=list(map(int,input().split()))
cnt=0
for i in range(N-1):
    if A*(X[i+1]-X[i])>B:
        cnt=cnt+B
    else:
        cnt=cnt+A*(X[i+1]-X[i])
print(cnt)