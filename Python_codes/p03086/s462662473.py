s=input()
acgt=["A","C","G","T"]
res=0
for i in range(len(s)):
    for j in range(i,len(s)):
        t=s[i:j+1]
        tmp=False
        for j in t:
            if not j in acgt:
                tmp=True
                break
        if tmp:
            continue
        res=max(res,len(t))
print(res)