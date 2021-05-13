n=int(input())
a=list(map(int,input().split()))
cnt = sum([1 for i in a if i < 0])
if cnt%2:
  r = 10**9
  for i in range(n):
    r = min(r,abs(a[i]))
  print(sum([abs(x) for x in a])-2*r)  
else:
  print(sum([abs(x) for x in a]))