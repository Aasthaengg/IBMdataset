N = int(input())
A = list(map(int, input().split()))
col = [0]*9

for a in A:
  if 1 <= a <= 399:
    col[0] += 1
  elif 400 <= a <= 799:
    col[1] += 1 
  elif 800 <= a <= 1199:
    col[2] += 1 
  elif 1200 <= a <= 1599:
    col[3] += 1
  elif 1600 <= a <= 1999:
    col[4] += 1
  elif 2000 <= a <= 2399:
    col[5] += 1
  elif 2400 <= a <= 2799:
    col[6] += 1
  elif 2800 <= a <= 3199:
    col[7] += 1
  elif 3200 <= a:
    col[8] += 1

ans = 0
if col[8] == N:
  print(1, N)
  exit()
  
for i in range(8):
  if col[i] > 0:
    ans += 1
print(ans, end=" ")
ans += col[8]
print(ans)