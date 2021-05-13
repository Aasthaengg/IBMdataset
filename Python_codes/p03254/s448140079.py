n,k = [int(i) for i in input().split()]
a = sorted([int(i) for i in input().split()])

sum = 0
count = 0
for i in a[:-1]:
  sum+=i
  if sum>k:
    break
  count+=1
if a[-1]==k-sum:
  count+=1
print(count)