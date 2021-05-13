import sys
input()
ans,d=0,{}
for ln in sys.stdin:
    s=''.join(sorted(ln))
    ans+=d.setdefault(s,0)
    d[s]+=1
print(ans)
