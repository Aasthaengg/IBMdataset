N = int(input())
l = [int(x) for x in range(1,N+1)]

total_num,max_num = 0,0

if N <= 2:
  print(N)
  exit()

for i in range(1,N):
  total_num += i
  if total_num >= N:
    max_num = i
    break

if total_num == N:
  for i in range(max_num):
    print(i+1)
else:
  ng_num = total_num - N
  for j in range(max_num):
    if j+1 != ng_num:
      print(j+1)