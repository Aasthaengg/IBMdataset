s=input()

s=list(s.replace("BC", "D"))
ans=0
cnt_a=0
for i in range(len(s)):
    if s[i]=="A":
        cnt_a+=1
    elif s[i]=="D":
        ans+=cnt_a
    else:
        cnt_a=0

print(ans)
