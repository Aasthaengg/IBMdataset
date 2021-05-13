A = int(input())
B = int(input())
C = int(input())
X = int(input())

X //= 50

res = 0

for i in range(A+1):
  rem = X-10*i
  if rem < 0:
    break
  for j in range(B+1):
    if 0 <= rem-2*j <= C:
      res += 1
      
print(res)