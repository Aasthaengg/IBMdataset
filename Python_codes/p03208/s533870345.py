
n,k=map(int,input().strip().split(" "))
ar=[]
for i in range(n):
    ar.append(int(input()))
ar.sort()
m=999999999999999

for i in range(n-k+1):

    c=ar[i+k-1]-ar[i]
    if c<m:
        m=c
print(m)