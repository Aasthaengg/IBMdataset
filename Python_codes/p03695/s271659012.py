def check_rate(r):
  for i,rate in enumerate(rates):
    if r < rate:
      return i

n=int(input())
a=list(map(int,input().split()))
rates=[400,800,1200,1600,2000,2400,2800,3200,float("inf")]
rates_cb=[False for _ in range(len(rates))]
wild=len(rates)-1
wild_c=0
for aa in a:
  r=check_rate(aa)
  if r == wild:
    wild_c+=1
  else:
    rates_cb[r]=True

base_col=rates_cb.count(True)
minc= max(1,base_col)
maxc=base_col+wild_c
print(minc,maxc)