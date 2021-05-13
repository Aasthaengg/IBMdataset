s=input()
t1=''
t2=''
ans=0
for c in s:
    t1+=c
    if t1!=t2:
        ans+=1
        t2=t1
        t1=''
print(ans)