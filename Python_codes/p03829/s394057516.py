N,A,B=(int(i) for i in input().split())
X=list(map(int,input().split()))
count=0

for i in range(N-1):
    M=(X[i+1]-X[i])*A
    if M<=B:
        count=count+M
    else:
        count=count+B
print(count)