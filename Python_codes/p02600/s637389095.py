inp = int(input())
if inp>=400 and inp<=599:
  ans = 8
elif inp>=600 and inp<=799:
  ans = 7
elif inp>=800 and inp<=999:
  ans = 6
elif inp>=1000 and inp<=1199:
  ans = 5
elif inp>=1200 and inp<=1399:
  ans = 4
elif inp>=1400 and inp<=1599:
  ans = 3
elif inp>=1600 and inp<=1799:
  ans = 2
elif inp>=1800 and inp<=1999:
  ans = 1
print(ans)