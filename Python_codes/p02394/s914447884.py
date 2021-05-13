m = map(int,raw_input().split())
if (0 <= m[2]-m[4])  and (m[2]+m[4] <= m[0]) and (0 <= m[3]-m[4]) and (m[3]+m[4] <= m[1]):
  print 'Yes'
else:
  print'No'