S=input()
ans=0
for i in S:
    if i=='+':
        ans+=1
    if i=='-':
        ans-=1
print(ans)