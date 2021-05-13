n,k = map(int,input().split())
a = list(map(int,input().split()))

#n,k = 10,3
#a = [5,1,3,2,4,1,1,2,3,4]

count = [0] * (n+1)
for i in a:
  count[i] += 1
count2 = []
for i in count:
  if i:
    count2.append(i)
count2 = sorted(count2)
target = len(count2) - k 
target = max(target,0)


ans = 0
if target:
  for i in range(target):
    ans += count2[i]
print(ans)