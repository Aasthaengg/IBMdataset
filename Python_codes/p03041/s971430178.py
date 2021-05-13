n,k=map(int,input().split())
S=input()
s=str.lower(S[k-1])
ans=S[:k-1]+s+S[k:]
print(ans)