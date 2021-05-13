N = int(input())
s = []
for i in range(N):
  tmp = list(input())
  tmp = sorted(tmp)
  s.append(''.join(tmp))
s = sorted(s)

i, j = 0, 1
count = 0
total = 0
while j < N:
  while s[i] == s[j]:
    count += 1
    j += 1
    if j == N:
      break
  
  if count == 1:
    total += 1
  elif count > 1:
    tmp1, tmp2 = 1, 2
    for k in range(count+1, count+1-2, -1):
      tmp1 *= k
    total += int(tmp1/tmp2)
  i = j
  j += 1
  count = 0

print(total)
