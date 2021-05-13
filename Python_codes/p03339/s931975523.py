n,s=open(0);a=t=s.count('E')
for i in s:t+=(-1 if i=='E' else 1);a=min(a,t)
print(a)