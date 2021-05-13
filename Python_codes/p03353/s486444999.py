s=list(input())
k1=int(input())
l1=set()
for i in range(len(s)):
    l1.add(s[i])
a1=[]
for i in range(len(l1)):
    a1.append(l1.pop())
a1.sort()
for i in range(len(a1)):
    str=a1[i]
    l2=set()
    for j in range(len(s)):
        if s[j]==str:
            l2.add(s[j])
            str2=s[j]
            for k in range(j+1,min(len(s),j+7)):
                str2+=s[k]
                l2.add(str2)
    if len(l2)>=k1:
        l3=sorted(l2)
        ans=l3[k1-1]
        break
    else:
        k1-=len(l2)
print(ans)
