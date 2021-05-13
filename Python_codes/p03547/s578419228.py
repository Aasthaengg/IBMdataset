p, q =input().split()
alpha ="ABCDEF"
p1=alpha.index(p)
p2 =alpha.index(q)
if p1>p2:
  print('>')
elif p1<p2:
  print('<')
else:
  print('=')