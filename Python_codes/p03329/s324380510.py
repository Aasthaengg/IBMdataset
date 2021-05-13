N = int(input())
l = [0] * (10**5+1)
nums = [0]
for i in range(N):
  tmp = []
  flag = False
  for k in nums:
    if l[k+1] == 0:
      l[k+1] = l[k]+1
      tmp.append(k+1)
    for j in range(1, N):
      if k+6**j <= N:
        if l[k+6**j] == 0:
          l[k+6**j] = l[k]+1
          tmp.append(k+6**j)
      else:
        break
    for j in range(1, N):
      if k+9**j <= N:
        if l[k+9**j] == 0:
          l[k+9**j] = l[k]+1
          tmp.append(k+9**j)
      else:
        break
    if l[N] > 0:
      flag = True
      break
  if flag:
    break
  else:
    nums = tmp
print(l[N])