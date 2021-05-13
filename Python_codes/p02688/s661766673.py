n, k = map(int, input().split())
ans = []
count = 0

for i in range(k):
  d = int(input())
  l = list(map(int, input().split()))
  for j in range(d):
    if l[j] not in ans:
      ans.append(l[j])

for i in range(n):
  if i+1 not in ans:
    count += 1
  
print(count)