n=int(input())
s=[]
for i in range(n):
    a=input()
    b=[]
    for j in range(10):
        b.append(a[j])
    b.sort()
    c="".join(b)
    s.append(c)
s.sort()
ans=0
t=1
for i in range(1,n):
    if s[i]==s[i-1]:
        ans+=t
        t+=1
    else:
        t=1
print(ans)