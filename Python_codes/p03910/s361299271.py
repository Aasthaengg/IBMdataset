n = int(input())
k = 0
while n > k:
  if k*(k+1)//2 < n <= (k+1)*(k+2)//2:
    break
  k += 1
s = (k+1)*(k+2)//2 - n
for i in range(1,k+2):
  if i == s:
    continue
  print(i)