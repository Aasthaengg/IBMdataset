n=int(input())
h=list(map(int,input().split()))

i=0
count=0
while i<=n-1:
    if h[i]==0:
        i+=1
    else:
        h[i]-=1
        count+=1
        k=i+1
        for l in range(k,n):
            if h[k]>0:
                h[k]-=1
                k+=1
            else:
                break

print(count)
