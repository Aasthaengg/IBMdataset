#ABC071 D - Coloring Dominoes
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
n=int(input())
s1=list(input())
s2=list(input())
i=0
mod=1000000007
 
ans=0
p=0
while i<n:
    if s1[i]==s2[i]:
        # 今回パターン1
        if p==0:
            ans=3
        elif p==1:
            ans*=2
            ans=ans%mod
        elif p==2:
            ans*=1
            ans=ans%mod
        i+=1
        p=1
    else:
        # 今回パターン2
        if p==0:
            ans=6
        elif p==1:
            ans*=2
            ans=ans%mod
        elif p==2:
            ans*=3
            ans=ans%mod
        i+=2
        p=2
print(ans)

