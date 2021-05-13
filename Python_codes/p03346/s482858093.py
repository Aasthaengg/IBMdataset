d={}
for x in map(int,open(0)):d[x]=d.get(x-1,0)+1
print(len(d)-max(d.values()))