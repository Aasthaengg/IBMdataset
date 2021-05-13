N=int(input())
a=list(map(int,input().split()))
x = 0
i = 0
while i<N-1:
    j=1
    while i<N-1 and a[i]==a[i+1]:
        j=j+1
        i=i+1
    i=i+1
    if j%2==1:
        x=x+(j-1)//2
    else:
        x=x+j//2
print(x)