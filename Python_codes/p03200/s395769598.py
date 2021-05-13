S=input()
ans=0
countB=0
for s in S:
    if s=='W':
        ans+=countB
    else:
        countB+=1
print(ans)