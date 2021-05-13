N=int(input())
d=sorted(list(map(int,input().split())))
if d[N//2-1]==d[(N//2)]:
  print(0)
else:
  print(d[N//2]-d[N//2-1])