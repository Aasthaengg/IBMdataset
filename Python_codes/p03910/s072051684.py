N = int(input())
n = 1
exclude = 0
while n*(n+1)//2 < N:
  n += 1
exclude = n*(n+1)//2-N
for num in range(n+1):
  if num == exclude or num == 0:
    continue
  else:
    print(num)