s=list(input())
c0=0
c1=0
for i in range(len(s)):
    if s[i]=="0":c0+=1
    else: c1+=1
print(2*min(c0,c1))
