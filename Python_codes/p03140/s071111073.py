n=int(input())
a=input()
b=input()
c=input()
a=list(a)
b=list(b)
c=list(c)
ans=0
for aa,bb,cc in zip(a,b,c):
    t=set()
    t.add(aa)
    t.add(bb)
    t.add(cc)
    ans+=len(t)-1
print(ans)
