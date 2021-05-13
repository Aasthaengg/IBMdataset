N = int(input())
P = 10**9+7
  
memo = [0]*(N+1)

for i in range(1,N+1):
  j = i
  while j % 2 == 0:
    memo[2] += 1
    j //= 2
  k = 3
  while k*k <= j:
    if j % k == 0:
      memo[k] += 1
      j //= k
    else:
      k += 2
  if j != 1:
    memo[j] += 1
  
rlt = 0
dic = {2:0, 4:0, 14:0, 24:0, 74:0}
for i in range(1, N+1):
  if memo[i] >= 74:
    dic[74] += 1
  if memo[i] >= 24:
    dic[24] += 1
  if memo[i] >= 14:
    dic[14] += 1
  if memo[i] >= 4:
    dic[4] += 1
  if memo[i] >=2:
    dic[2] += 1
    

rlt += dic[74]
rlt += dic[24]*(dic[2]-1)
rlt += dic[14]*(dic[4]-1)
rlt += dic[4]*(dic[4]-1)*(dic[2]-2)//2

print(rlt)