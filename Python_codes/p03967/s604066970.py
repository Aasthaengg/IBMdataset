s=input()
now=0
ans=0
for i in s:
    if now:
        now-=1
        if i=="g":
            ans+=1
    else:
        now+=1
        if i=="p":
            ans-=1
print(ans)