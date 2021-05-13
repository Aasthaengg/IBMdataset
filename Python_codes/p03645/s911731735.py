n,m=map(int,input().split())
sa=set()
sb=set()
for i in range(m):
    a,b=map(int,input().split())
    if a==1:
        sb.add(b)
    if b==n:
        sa.add(a)
print("IMPOSSIBLE" if len(sa&sb)==0 else "POSSIBLE")