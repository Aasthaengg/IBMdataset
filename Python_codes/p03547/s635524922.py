a,b=input().split()
g={'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
if a==b:
  print('=')
elif g[a] > g[b]:
  print('>')
elif g[a] < g[b]:
  print('<')