N = int(input())
count = 0

for a in range(1, N):
  tmp = (N-1) // a
  if a <= (N) // 2:
    count += tmp
  else:
    count += 1          

print(count)