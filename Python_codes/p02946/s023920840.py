k, x = map(int,input().split())
l = list(range(x-k+1,x+k,1))
for x in l:
  print(x, end=' ')