ss=input().strip()
d={}
for s in ss:
  d[s]=d.get(s,0)+1

flg=False
for s in ss:
  if d[s]!=2:
    flg=True
print("No" if flg else "Yes")
