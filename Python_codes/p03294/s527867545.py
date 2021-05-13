import fractions
n=int(input())
A=list(map(int,input().split()))
gd=1
tmp=A[0]
for i in range(n-1):
    gd=fractions.gcd(A[i+1],A[i])
    tmp*=A[i+1]
lcm=tmp//gd
lcm-=1
ans=0
for a in A:
    ans+=lcm%a

print(ans)