N=int(input())
ans=0
i=1
while i**2<N:
    if N%i==0:
        if i>1 and N//(i-1)==N%(i-1):
            ans+=i-1
        j=N//i
        if j!=i and N//(j-1)==N%(j-1):
            ans+=j-1
    i+=1
print(ans)