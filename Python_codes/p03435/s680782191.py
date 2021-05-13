c = [list(map(int,input().split())), 
     list(map(int,input().split())), 
     list(map(int,input().split()))]
if c[0][0]-c[1][0] != c[0][1]-c[1][1] or c[0][1]-c[1][1] != c[0][2]-c[1][2]:
  print('No')
elif c[1][0]-c[2][0] != c[1][1]-c[2][1] or c[1][1]-c[2][1] != c[1][2]-c[2][2]:
  print('No')
else:
  print('Yes')