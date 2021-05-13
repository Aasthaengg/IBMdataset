N=int(input())
a=list(map(int,input().split()))

Q=0
for i in range(N-1):
    if a[i]==a[i+1]:
        a[i+1]=0
        Q+=1
print(Q)