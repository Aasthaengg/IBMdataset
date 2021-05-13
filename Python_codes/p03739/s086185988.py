n = int(input())
a = list(map(int,input().split()))
sum = 0
res = [0,0]
for change in range(2):
  sum = 0
  for i in range(n):
    if i % 2 == change:
      if sum + a[i] < 0: # -だったら
        #temp = -1 - sum - a[i]
        temp = 1 - sum - a[i]
        res[change] += temp
        sum += temp
      elif sum + a[i] == 0:
        sum += 1
        res[change] += 1
    else:
      if sum + a[i] > 0:
        #temp = 1 - sum - a[i]
        temp = -1 - sum - a[i]
        res[change] -= temp
        sum += temp
      elif sum + a[i] == 0:
        sum -= 1
        res[change] += 1
    sum += a[i]
print(min(res[0],res[1]))