n = int(input())
ans = n
for i in range(n // 2):
  j = i + 1
  k = n - j
  sumj = []
  sumk = []
  for l in range(len(str(j))):
    strj = str(j)
    sumj.append(int(strj[l]))
    
  for l in range(len(str(k))):
    strk = str(k)
    sumk.append(int(strk[l]))
  if sum(sumj) + sum(sumk) < ans:
    ans = sum(sumj) + sum(sumk)
print(ans)