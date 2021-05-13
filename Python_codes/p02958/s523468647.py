n = int(input())
p = list(map(int,input().split()))
count = 0

sort_p = sorted(p)

for i in range(n):
  if p[i] != sort_p[i]:
    count += 1
    
if count  == 2:
  print("YES")
  exit()
elif count == 0:
  print("YES")
  exit()
else:
  print("NO")
  exit()
