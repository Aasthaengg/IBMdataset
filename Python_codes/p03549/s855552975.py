n,m=map(int,input().split())
ans=0
s=2**m
ans=((n-m)*100+m*1900)*s
print(ans)