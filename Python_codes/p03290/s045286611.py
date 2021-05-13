d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

pc = pc[::-1]
#print(pc)
ans = float('inf')
for i in range(2**d):
  total = 0
  cnt = 0
  for j in range(d):
    if (i>>j) & 1:
      total += 100*(d-j)*pc[j][0] + pc[j][1]
      cnt += pc[j][0]
    if total >= g:
      ans = min(ans, cnt)
      continue
  for j in range(d):
    if (i>>j) & 1 == False:
      for k in range(pc[j][0]):
        total += 100*(d-j)
        cnt += 1
        if total >= g:
          ans = min(ans, cnt)
          break
      break
      
print(ans)