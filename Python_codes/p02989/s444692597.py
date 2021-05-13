n=int(input())
d=list(map(int,input().split()))
d.sort()
dd=len(d)
if dd%2 ==0:
  print(d[dd//2]-d[dd//2-1])
else:
  print(0)
