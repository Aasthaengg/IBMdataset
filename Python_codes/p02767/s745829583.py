n = int(input())
x = list(map(int, input().split()))
x.sort()
res = 10**7
for i in range(x[0],x[-1]+1):
  tmp = 0
  for j in x:
    tmp += (j-i)**2
  res = min(tmp,res)
print(res)