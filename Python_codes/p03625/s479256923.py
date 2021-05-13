n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
H=0
W=0
i=0
while i<n-1:
    if a[i]==a[i+1]:
        if H==0:
            H=a[i]
            i+=2
        else:
            W=a[i]
            break
    else:
        i+=1
print(H*W)