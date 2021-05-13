s=input()
s_len=len(s)
ans="No"
for i in range(s_len-1):
    if s[i]=="C":
        if "F" in s[i+1:]:
            ans="Yes"
print(ans)