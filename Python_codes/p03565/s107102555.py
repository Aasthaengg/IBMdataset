s,t=input(),input()
start=len(s)-len(t)
flag=1
if start<0: print("UNRESTORABLE")
else:
    while start>=0:
        flag=1
        for i in range(len(t)):
            if s[start+i]!="?" and s[start+i]!=t[i]:
                flag=0
                break
        if flag:
            s=s[0:start]+t[:]+s[start+len(t):len(s)]
            s=s.replace("?","a")
            break
        start-=1
    if flag: print(s)
    else: print("UNRESTORABLE")