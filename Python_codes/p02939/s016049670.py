A=input()
ans=0
before=""
c=""
for i in A:
    c+=i
    if c != before:
        before=c
        c=""
        ans+=1
print(ans)