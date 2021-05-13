n=int(input())
s=[]
p=[]
for i in range(n):
    si,pi=input().split()
    s.append(si)
    p.append(int(pi))
ans=[0]*n
for i in range(n-1):
    for j in range(i+1,n):
        if s[i]>s[j]:
            ans[i]+=1
        elif s[i]<s[j]:
            ans[j]+=1
        else:
            if p[i]<p[j]:
                ans[i]+=1
            else:
                ans[j]+=1
z=[0]*n
for i in range(n):
    z[ans[i]]=(i+1)
for i in range(n):
    print(z[i])