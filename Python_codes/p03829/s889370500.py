N,A,B=map(int,input().split())
X=list(map(int,input().split()))

ans=0
pre=X[0]

for xi in X[1:]:
    if (xi-pre)*A-B>0:
        ans+=B
    else:
        ans+=(xi-pre)*A
    pre=xi

print(ans)