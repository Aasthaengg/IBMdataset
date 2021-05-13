n=int(input())

p=list(map(int, input().split()))
pm=max(p)
p.remove(pm)
if pm<sum(p):
  print('Yes')
else:
  print('No')