s=input()

n=10000000
for i in range(26):
    lis=[-1]
    for c in range(len(s)):
        if s[c]==chr(ord("a")+i):
            lis.append(c)
    if len(lis)>1:
        ni=0
        for j in range(len(lis)-1):
            ni=max(ni,lis[j+1]-lis[j]-1)
        ni=max(ni,len(s)-1-lis[len(lis)-1])
        n=min(n,ni)

print(n)