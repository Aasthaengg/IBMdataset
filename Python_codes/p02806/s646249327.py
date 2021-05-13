n=int(input())
s=[]
t=[]
for i in range(n):
    ts,tt=input().split()
    s.append(ts)
    t.append(int(tt))
x=input()
ans=0
ok=False
for i in range(n):
    if ok:
        ans += t[i]
    if s[i]==x:
        ok=True
print(ans)