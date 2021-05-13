sv,hm=map(int,input().split())
i=list(map(int,input().split()))
sum=0

for j in range(hm):
  sum+=i[j]
  
if sv-sum>=0:
  print(sv-sum)
else:
  print("-1")

