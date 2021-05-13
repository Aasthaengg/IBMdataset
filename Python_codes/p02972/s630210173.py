N=int(input())
a=list(map(int,input().split()))
b=[0 for _ in range(N)]
for i in range(N):
    j=N-1-i
    if sum(b[j:N:j+1])%2!=a[j]:
        b[j]=1

print(sum(b))
for k in range(N):
    if b[k]==1:
        if k<N-1:
            print(k+1,end=" ")
        else:
            print(k+1)