s,t=input(),input()
ss,ts=[set()for i in range(26)],[set()for i in range(26)]
sc={}
tc={}
for i in range(len(s)):
    if s[i]not in sc:
        if t[i] in tc:print("No");exit()
        else:
            d=len(sc)
            ss[d].add(i)
            ts[d].add(i)
            tc[t[i]]=d
            sc[s[i]]=d
    else:
        if t[i]not in tc or sc[s[i]]!=tc[t[i]]:print("No");exit()
        else:
            ss[sc[s[i]]].add(i)
            ts[sc[s[i]]].add(i)
for i in range(26):
    if ss[i]!=ts[i]:print("No");break
else:print("Yes")