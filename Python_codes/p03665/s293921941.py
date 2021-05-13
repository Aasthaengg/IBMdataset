N,P = map(int,input().split())
A = list(map(int,input().split()))

A = [a % 2 for a in A]

acc = [1] * 60
for i in range(60):
  if i == 0:
    continue
  acc[i] = acc[i-1] * i

odd = sum(A)
even = N - odd

ans = 0
if P == 0:
  # 奇数から偶数個
  j = 0
  for i in range(0,odd+1,2):
    j += acc[odd] // (acc[odd-i] * acc[i])

else:
  # 奇数から奇数個
  j = 0
  for i in range(1,odd+1,2):
    j += acc[odd] // (acc[odd-i] * acc[i])
  
ans = 0
for i in range(even+1):
  k = acc[even] // (acc[even-i] * acc[i])
  ans += k * j
  
print(ans)
                        
