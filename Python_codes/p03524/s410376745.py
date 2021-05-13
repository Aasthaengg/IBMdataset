s=input()
d={"a":0,"b":0,"c":0}
for m in s:
  d[m]+=1
if max(d["a"],d["b"],d["c"])-min(d["a"],d["b"],d["c"])>1:
  print("NO")
else:
  print("YES")
 
