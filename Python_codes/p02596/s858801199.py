k=int(input())
ans=[0]*(k+1)
ans[0] = 7
if 7 % k == 0:
  print(1)
  quit()
for i in range(1,k):
  ans[i] += ((10*ans[i-1]+7)%k)
  if ans[i] % k == 0:
    print(i+1)
    break
else:
  print(-1)