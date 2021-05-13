prime_list = [2]
N = int(input())
A = [0] * N

for i in range(3,10**3+1):
  flag = True
  for j in range(2,int(i**0.5)+1):
    if i % j == 0:
      flag = False
      break
  if flag:
    prime_list.append(i)

for i in range(1,N+1):
  # 素因数分解してAにぶち込む
  tmpN = i
  for j in prime_list:
    while tmpN % j == 0:
      A[j-1] += 1
      tmpN //= j
ans = 1
p = 10**9 + 7
for i in range(1,N):
  ans *= (A[i] + 1)
  ans %= p
print(ans)