n = int(input())
d = list(map(int,input().split()))
d = sorted(d)
length = len(d)
half1 = d[int(length/2)-1]
half2 = d[int(length/2)]
if half1 == half2:
  print(0)
else:
  print(half2-half1)