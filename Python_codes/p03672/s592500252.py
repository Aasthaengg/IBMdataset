s=input()
ans=0
for i in range(len(s)//2):
    t1=s[0:i]
    t2=s[i:2*i]
    if t1==t2:
#        print(t1,t2)
        ans=max(ans,2*i)
print(ans)