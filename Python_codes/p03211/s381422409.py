S=int(input())
ans=10**9
while S>=100:
    ans=min(ans,abs(S%1000-753))
    S//=10
print(ans)
