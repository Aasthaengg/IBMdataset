n = int(input())
d = []
for i in range(n):
  a = list(map(int, input().split()))
  d.append(a)
total = 0
for i in d:
  if i[0] == i[1]:
    total += 1
  else:
    total = 0
  
  if total == 3:
    print("Yes")
    exit()

print("No")
    
