a,b,c,k = map(int,input().split())
ans=0
if a>=k:
    ans=ｋ
else:
    k-=a
    if b>=k:
        ans=a
    else:
        k-=b
        ans=a-k
print(ans)