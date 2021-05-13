N,x = map(int,input().split())
a = sorted(list(map(int,input().split())))
s = [sum(a[:i+1]) for i in range(N)]

if s[-1] == x:
  print(N)
  exit()
else:
  for i in range(N-1):
    if s[i] > x:
      print(i)
      exit()
      
  print(N-1)