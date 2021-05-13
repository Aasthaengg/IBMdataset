n=int(input())
d=[int(x) for x in input().rstrip().split()]
d.sort()
ind=n//2

if d[ind-1]==d[ind]:
  print(0)

else:
  print(d[ind]-d[ind-1])

