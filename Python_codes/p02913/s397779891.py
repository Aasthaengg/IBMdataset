n=int(input())
s=input()

def ZA(n,s):
    Z=[0 for i in range(n)]
    Z[0]=n
    i=1
    j=0
    cand=0
    while i<n:
        while i+j<n and s[j]==s[i+j]:
            j+=1
        Z[i]=j
        cand=max(cand,min(Z[i],i))
        if j==0:
            i+=1
            continue
        k=1
        while k<j and k+Z[k]<j:
            Z[i+k]=Z[k]
            cand=max(cand,min(Z[i],i))
            k+=1
        i+=k
        j-=k
    #print(Z)
    return cand


ans=0
for i in range(n):
    ans=max(ans,ZA(n-i,s[i:]))
print(ans)