a,b = map(str,input().split())
List = ['A','B','C','D','E','F']
x =List.index(a)
y = List.index(b)
if x > y:
  print('>')
elif x ==y:
  print('=')
else:
  print('<')