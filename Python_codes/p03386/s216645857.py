a,b,k = tuple(map(int,input().split()))
s = set([])
for i in range(min(k,b-a+1)):
  s.add(a+i)
  s.add(b-i)

  
s = sorted(list(s))
for i in s:
  print(i)
