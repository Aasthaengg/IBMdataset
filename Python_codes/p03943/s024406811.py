a,b,c = map(int,input().split())

l = [a,b,c]

abc = sum(l)/2

if abc in l:
  print('Yes')
else:
  print('No')