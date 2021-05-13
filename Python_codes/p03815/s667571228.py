x = int(input())
m = 11
if x < 7:
  ans = 1
elif x <= 11:
  ans = 2
elif x%m == 0:
  ans = x*2//m
elif 0 < x%m <= 6:
  ans = (x//m)*2+1
elif 7 <= x%m:
  ans = (x//m)*2+2
print(ans)