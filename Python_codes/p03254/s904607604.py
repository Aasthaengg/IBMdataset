N,x = map(int,input().split())
AAA = map(int,input().split())
AA = list(AAA)
AA.sort()
total = 0
count =0
for i in AA:
  total += i
if total == x:
  ans = N
elif total < x:
  ans = N-1
else:
  for i in AA:
    if x >= i:
      x -= i
      count +=1
  ans = count
print(ans)