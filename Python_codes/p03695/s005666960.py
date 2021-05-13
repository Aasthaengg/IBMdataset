n = int(input())
a = list(map(int, input().split()))

rate = [0 for _ in range(9)]
#print(rate)
for i in a:
  if 1<=i<=399:
    rate[0]+=1
  elif 400<=i<=799:
    rate[1]+=1
  elif 800<=i<=1199:
    rate[2]+=1
  elif 1200<=i<=1599:
    rate[3]+=1
  elif 1600<=i<=1999:
    rate[4]+=1
  elif 2000<=i<=2399:
    rate[5]+=1
  elif 2400<=i<=2799:
    rate[6]+=1
  elif 2800<=i<=3199:
    rate[7]+=1
  else:
    rate[8]+=1
    
#print(rate)

ans = 0

for j in range(8):
  if rate[j] != 0:
    ans += 1
if ans!=0:
  print(ans, ans+rate[8])
else:
  print(1, rate[8])