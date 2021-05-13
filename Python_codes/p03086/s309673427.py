S=input()
ans=cur=0
for c in S:
    if c in 'ACGT':
        cur+=1
        ans=max(ans,cur)
    else:
        cur=0
print(ans)
