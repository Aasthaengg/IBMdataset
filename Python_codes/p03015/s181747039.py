l = input()
m = 10**9+7
ans = 0
c = 1
while len(l) > 1:
  ans = (ans+c*pow(3,len(l)-1,m))%m
  j = 1
  while l[j] == '0':
    j += 1
    if j == len(l):
      j -= 1
      break
  l = l[j:]
  c = (2*c)%m
ans = (ans+(2*int(l)+1)*c)%m
print(ans)