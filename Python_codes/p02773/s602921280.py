n,*s=map(str,open(0).read().split())
mydict={}
for i in set(s):
    mydict[i]=1
for i in s:
    mydict[i]+=1
    """
    if s[i] in mydict:
        mydict[s[i]]+=1
    else:
        mydict[s[i]]=1
    """
v_max=max(mydict.values())
for i in sorted([kv[0] for kv in mydict.items() if kv[1]==v_max]):
    print(i)