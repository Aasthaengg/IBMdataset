n=int(input())
a=list(map(int, input().split()))
mon=1000
kai=0
for i in range(n-1):
  if a[i]>a[i+1]:
    mon+=kai*a[i]
    kai=0
  elif a[i]<a[i+1] and kai==0:
    kai=int(mon/a[i])
    mon-=kai*a[i]

mon+=kai*a[n-1]

print(mon)
