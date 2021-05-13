w,a,b=map(int,input().split())
if a<=b<=a+w or a<=b+w<=a+w:
  print(0)
else:
  print(min(abs(b-(a+w)),abs(a-(b+w))))


