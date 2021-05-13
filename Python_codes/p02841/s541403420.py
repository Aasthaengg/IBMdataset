import datetime

M,D = map(int,raw_input().split())
ans = format((datetime.date(2019, M, D) + datetime.timedelta(days = 1)).day)

if int(ans) == 1:
  print "1"
else:
  print "0"