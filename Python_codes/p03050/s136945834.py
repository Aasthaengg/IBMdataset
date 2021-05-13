N=int(input())
ans=0
if N==1:
    ans=0
else:
    for i in range(1,int(N**0.5)+1):
        if (N-i)%i==0:
            q=(N-i)//i
            if N%q==i:
                ans+=(N-i)//i
print(ans)