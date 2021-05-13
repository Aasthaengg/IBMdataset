N = int(input())
H = list(map(int,input().split()))
count = 0
count_max = 0
for i in range(N-1):
  if H[i]>=H[i+1]:
    count = count+1
  elif H[i]<=H[i+1] and count_max<count:
    count_max = count
    count = 0
  else:
    count = 0
if count_max>count:
  print(count_max)
else:
  print(count)