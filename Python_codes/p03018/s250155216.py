s=input()
s=s.replace("BC","D")
s=s.replace("B"," ")
s=s.replace("C"," ")
s=list(s.split())
ans=0
for u in s:
    if u:
        u=list(u)
        count=0
        cnt=0
        for i in range(len(u)):
            if u[i]=="D":
                count+=i
                cnt+=1
        ans+=count-cnt*(cnt-1)//2
print(ans)