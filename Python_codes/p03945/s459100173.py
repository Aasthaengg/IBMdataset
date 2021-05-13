s=input()
c1=s[0]
res=0
for c in s:
    if c==c1:
        continue
    else:
        res+=1
        c1=c
print(res)