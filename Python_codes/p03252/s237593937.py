s=input()
t=input()
s1={}
t1={}
for i in range(len(s)):
    if s[i] in s1 and t[i] in t1:
        if s1[s[i]]!=t1[t[i]]:
            print("No")
            break
    elif s[i] not in s1 and t[i] not in t1:
        s1[s[i]]=i
        t1[t[i]]=i
    else:
        print("No")
        break
else:
    print("Yes")