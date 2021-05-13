n = int(input())
lst = [0, 0, 0, 0, 0]
for i in range(n):
  s = input()
  if s[0] == "M":
    lst[0] += 1
  if s[0] == "A":
    lst[1] += 1
  if s[0] == "R":
    lst[2] += 1
  if s[0] == "C":
    lst[3] += 1
  if s[0] == "H":
    lst[4] += 1

ans = 0
for i in range(3):
  for j in range(i+1, 4):
    for k in range(j+1, 5):
      ans += lst[i]*lst[j]*lst[k]
      
print(ans)