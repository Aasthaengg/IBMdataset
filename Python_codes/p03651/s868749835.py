import fractions
N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
m=A[-1]
if m<K:
    print("IMPOSSIBLE")
else:
    ans=A[0]
    for i in range(1,N):
        ans=fractions.gcd(ans,A[i])
    if fractions.gcd(K,ans)==ans:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")