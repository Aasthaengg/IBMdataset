n, m = map(int, input().split())
an = [int(num) for num in input().split()]

check = sum(an)/(4*m)
count = 0

for a in an :
  if a >= check:
    count += 1

if count >= m:
  print("Yes")
else :
  print("No")