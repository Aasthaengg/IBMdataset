from collections import defaultdict as d
s=d(int)
s[0]=0
n,w=map(int,input().split())
for i in range(n):
    q,v=map(int,input().split())
    c=s.copy()
    for p,r in c.items():
        if p+q<=w:
            s[p+q]=max(s[p+q],r+v)
print(max(s.values()))