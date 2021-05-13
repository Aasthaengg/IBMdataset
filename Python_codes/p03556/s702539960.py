N=int(input())
a=1
for i in range(int(10**4.6)):
    if i**2<=N:
        ans=max(a,i**2)
print(ans)