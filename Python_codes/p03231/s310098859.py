def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

N,M=map(int,input().split())
S=input()
T=input()

C=N*M//gcd(max(N,M),min(N,M))
n=C//N
m=C//M

i=0
j=0
ans=C
while i<C and j<C:
    if  i==j:
        if S[i//n]!=T[j//m]:
            ans=-1
        i+=n
        j+=m
    elif i<j:
        i+=n
    else:
        j+=m
print(ans)