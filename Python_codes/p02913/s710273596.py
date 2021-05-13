def z_algorithm(S):
    l=len(S)
    A=[0]*n
    i=1;j=0
    while i<l:
        while(i+j<l and S[j]==S[i+j]):
            j+=1
        A[i]=j
        if j==0:
            i+=1
            continue
        k=1
        while i+k<l and k+A[k]<j:
            A[i+k]=A[k]
            k+=1
        i+=k
        j-=k
    return A
n=int(input())
s=input()
ans=0
for i in range(n-1):
    a=z_algorithm(s[i:])
    for j in range(len(a)):
        if(a[j]<=j):
            ans=max(ans,a[j])
print(ans)