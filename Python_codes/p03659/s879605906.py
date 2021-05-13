N=int(input())
a=list(map(int,input().split()))

ans=2*10**9+10
s=sum(a)
now=0
snuke=0
for i in range(N-1):
    snuke+=a[i]
    now=s-2*snuke

    ans=min(abs(now),ans)

print(ans)