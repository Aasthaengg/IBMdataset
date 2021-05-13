S=input()
ans=len(S)
now=S[0]
for s in S:
    ans-=s==now
    now=s
print(ans)