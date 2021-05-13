S=input()
cnt=0
ans=0

for s in S:
    if s=='B':
        cnt+=1
    else:
        ans+=cnt
print(ans)   