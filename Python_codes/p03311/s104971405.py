n=int(input())
a=sorted([x-i for i,x in enumerate(list(map(int,input().split())))])
if n%2==1:
  print(sum([abs(x-a[n//2]) for x in a]))
else:
  print(min(sum([abs(x-a[n//2]) for x in a]),sum([abs(x-a[n//2+1]) for x in a])))
