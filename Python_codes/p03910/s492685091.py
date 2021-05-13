n = int(input())
k = 1
while True:
  if k*(k+1)//2 >= n:
    ans = k
    break
  k += 1
if n == ans*(ans+1)//2:
  i = 1
  while i <= ans:
    print(i)
    i += 1
else:
  i = 1
  l = []
  cnt = 1
  while i < ans:
    if cnt <= (ans-1)*(ans+2)//2 - n:
      print(i)
      cnt += 1
    else:
      print(i+1)
    i += 1
    

