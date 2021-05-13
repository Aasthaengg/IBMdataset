s=list(input())
ans=0
g_c,p_c=0,0
for i in range(len(s)):
    if i==0:
        g_c+=1
        if s[i]=='p':
            ans-=1
        continue
    if s[i]=='g':
        if p_c<g_c:
            p_c+=1
            ans+=1
        else:
            g_c+=1
    else:
        if p_c<g_c:
            p_c+=1
        else:
            g_c+=1
            ans-=1
print(ans)