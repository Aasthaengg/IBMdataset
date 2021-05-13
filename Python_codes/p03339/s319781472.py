n=int(input())
s=list(input())

w=s.count('W')
e=s.count('E')
r_w=w
r_e=e
l_w=0
l_e=0
ans=n

for i in range(n):
    if s[i]=='W':
        r_w-=1
        tmp=l_w+r_e
        l_w+=1
    else:
        r_e-=1
        tmp=l_w+r_e
        l_e+=1
    if tmp<ans:
        ans=tmp
print(ans)