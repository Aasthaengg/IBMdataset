n = int(input())
a = list(map(int,input().split()))
wa = 1
ka = 0
if(a.count(0)>=1):
  print(0)
  ka +=1
else:
  for i in range(n):
    wa = wa*a[i]
    if(wa>10**18):
      print("-1")
      ka +=1
      break
if(ka==0):
  print(wa)

