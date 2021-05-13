s = input()
s = s.split()
n = int(s[0])
k = int(s[1])

if n==1:
  print(k)
elif n==2:
  print(k*(k-1))
else:
  ans = k
  for i in range(n-1):
    ans = ans*(k-1)
  print(ans)
