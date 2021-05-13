sa=input();sb=input();sc=input()
s=[1,0,0]
ss=[sa,sb,sc]
now = sa[0]

la=len(sa);lb=len(sb);lc=len(sc)
ans=["A","B","C"]
l=[la,lb,lc]
if la<=1:
    print("A")
    exit()

p2n={'a':0,'b':1,'c':2}

while 1:
    nxt=p2n[now]
    if s[nxt]>=l[nxt]:
        print(ans[nxt])
        exit()
    tmp=ss[nxt][s[nxt]]
    s[nxt]+=1
    now=tmp