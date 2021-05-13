n,a,b,c=int(input()),input(),input(),input()
ans=0
for i in range(n):
    s=set()
    s.add(a[i]);s.add(b[i]);s.add(c[i])
    ans+=len(s)-1
print(ans)