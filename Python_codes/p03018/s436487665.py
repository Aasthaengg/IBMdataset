s = input()
a_cnt=0
ans=0
i=0
while i < len(s)-1:
    if s[i] == "A":
        a_cnt+=1
        i+=1
    elif s[i] == "B" and s[i+1] == "C":
        ans+=a_cnt
        i+=2
    else:
        a_cnt=0
        i+=1
print(ans)