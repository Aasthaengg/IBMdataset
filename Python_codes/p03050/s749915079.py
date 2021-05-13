N=int(input())
sqrtn=int(N**0.5)
ans=0
for r in range(1,sqrtn+1):
    if N%r==0 and N/r-1>r:
        ans+=(int(N/r)-1)
print(int(ans))
