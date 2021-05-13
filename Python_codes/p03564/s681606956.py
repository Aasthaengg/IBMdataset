N,K=int(input()),int(input())
num = 1
for i in range(N):
  if num < K:
    num *= 2
  else:
    num += K
print(num)