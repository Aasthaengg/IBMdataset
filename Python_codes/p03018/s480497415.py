s=input()
s=s.replace("BC","D")
n=len(s)
ans=0
cnt=0
for i in range(n-1,-1,-1):
    if s[i]=="B" or s[i]=="C":
        cnt=0
    elif s[i]=="D":
        cnt+=1
    else:
        ans+=cnt
print(ans)
