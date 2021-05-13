k,s = map(int,input().split())
count = 0
for i in range(k+1):
  a = s - i
  for j in range(k+1):
    b = s - i - j
    if 0 <= b <= k:
      count +=1

print(count)