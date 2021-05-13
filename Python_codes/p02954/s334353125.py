s=input()
ans=[0]*(len(s))

now="R"
r=[0]*2
l=[0]*2
for i in range(len(s)):
    if now=="R":
        if s[i]=="R":
            r[i%2]+=1
        else:       
            ans[i]+=r[i%2]
            ans[i-1]+=r[(i+1)%2]
            now="L"
            r=[0]*2
            pos=i
            l[i%2]+=1
    else:
        if s[i]=="L":
            l[i%2]+=1
        else:
            ans[pos]+=l[pos%2]
            ans[pos-1]+=l[(pos+1)%2]
            now="R"
            l=[0]*2
            r[i%2]+=1

ans[pos]+=l[pos%2]
ans[pos-1]+=l[(pos+1)%2]

L=[str(a) for a in ans]
ans=" ".join(L)
print(ans)
