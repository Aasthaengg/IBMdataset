n = int(input())
s = []
for i in range(n):
  s.append(int(input()))
  
sums = sum(s)
s.sort()

if sums%10 != 0:
  print(sums)
  exit()
  
for i in s:
  if i%10 != 0:
    sums -= i
    print(sums)
    exit()
    
print(0)
