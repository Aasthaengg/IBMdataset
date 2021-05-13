n,a,b,c,d=map(int,input().split())
s=input()
ans="Yes"
if c<b:
    for i in range(a-1,c-1):
        if s[i]=="#" and s[i+1]=="#":
            ans="No"
            break
    if ans=="Yes":
        for i in range(b-1,d-1):
            if s[i]=="#" and s[i+1]=="#":
                ans="No"
                break
elif c<d:
    for i in range(a-1,d-1):
        if s[i]=="#" and s[i+1]=="#":
            ans="No"
            break
else:
    cnt=0
    for i in range(a-1,c-1):
        if s[i]=="#" and s[i+1]=="#":
            ans="No"
            break
    if ans=="Yes":
        for i in range(b-2,d+1):
            if s[i]==".":
                cnt+=1
                if cnt==3:
                    break
            else:
                cnt=0
        if cnt!=3:
            ans="No"
print(ans)