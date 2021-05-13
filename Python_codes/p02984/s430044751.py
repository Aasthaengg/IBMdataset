n=int(input())
a=list(map(int,input().split()))

b=[0]*n
oddsum=0
evensum=0
for i in range(n):
    if i%2==0:
        oddsum+=a[i]
    else:
        evensum+=a[i]

b[0]=oddsum-evensum

for i in range(1,n):
    c=b[i-1]-a[i-1]
    b[i]=-c
    b[i]+=a[i-1]

L=[str(a) for a in b]
ans=" ".join(L)
print(ans)