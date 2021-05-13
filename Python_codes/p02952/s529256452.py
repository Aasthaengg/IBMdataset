N=list(input())
ans=0
for i in range(len(N)):
    if i==len(N)-1:
        if len(N)%2==1:
            s=""
            for num in N:
                s=s+num
            s=int(s)-10**i
            s+=1
            ans+=s
    else:
        if i%2==0:
            ans+=10**(i+1)-10**i
print(ans)