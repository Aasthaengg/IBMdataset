n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
ans=a[0]
for i in range(n-1):
    ans+=(2**i)*a[i+1]
print(ans/(2**(n-1)))
    
