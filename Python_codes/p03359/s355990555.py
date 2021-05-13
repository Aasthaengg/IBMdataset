m=[31,28,31,30,31,30,31,31,30,31,30,31]
a,b=map(int,input().split())
ans=0
for month in range(a):
  for day in range(m[month]):
    if month==a-1 and day+1>b:
      break
    if month==day:
      ans+=1
print(ans)
