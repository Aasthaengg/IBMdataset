from collections import defaultdict
s=list(input())
t=list(input())
change_st=defaultdict(int)
change_ts=defaultdict(int)
for i in range(len(s)):
    if change_st[s[i]]==0:
        change_st[s[i]]=t[i]
    else:
        if change_st[s[i]]!=t[i]:
            print("No")
            break
    if change_ts[t[i]]==0:
        change_ts[t[i]]=s[i]
    else:
        if change_ts[t[i]]!=s[i]:
            print("No")
            break
else:
    print("Yes")
        
