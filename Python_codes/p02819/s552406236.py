n=int(input())
while True:
  judge=False
  count = 0
  for i in range(2, n):
    if n%i==0:
      n+=1
      judge=True
      break
  if judge: continue
  print(n)
  break