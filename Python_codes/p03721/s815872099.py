n,m = map(int,input().split()); sus = {}
for _ in range(n):
  a,b = map(int,input().split())
  sus[a] = sus[a]+b if a in sus else b
fef = sorted(sus.items()); snaas = 0
for cuc in fef:
  snaas += cuc[1]
  if snaas >= m: print(cuc[0]); exit()