n=int(input())
a=list(map(int,input().split()))

x=[0]*(10**6+1)
for i in a:
    x[i]+=1


for i in range(10**6+1):
    if x[i]>=1:
        j=2
        while i*j<=10**6:
            x[i*j]=0
            j+=1
print(x.count(1))
