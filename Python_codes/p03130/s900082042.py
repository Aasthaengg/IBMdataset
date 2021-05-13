d={}
for k in map(int,open(0).read().split()):d[k]=d.get(k,0)+1
for v in d.values():
 if v>2:print("NO");quit()
print("YES")