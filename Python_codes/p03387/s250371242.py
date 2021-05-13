abc = sorted(list(map(int, input().split())))

if (abc[0]%2==0 and abc[1]%2==0) or (abc[0]%2==1 and abc[1]%2==1):
  ans = 0
  ans += abc[2]-abc[1]
  ans += (abc[1]-abc[0])//2
  print(ans)
else:
  count = 0
  for i in abc:
    if i%2 == 0: count+=1

  for i in range(len(abc)):
    if count == 2:
      if abc[i]%2 == 0: abc[i] += 1
    else:
      if abc[i]%2 == 1: abc[i] += 1
  ans = 1
  ans += abc[2]-abc[1]
  ans += (abc[1]-abc[0])//2
  print(ans)