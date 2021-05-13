N = int(input())
a = list(map(int,input().split()))

odd = 0
double = 0
quatro = 0

for i in a:
  if i % 2 == 1:
    odd += 1
  else:
    if i % 4 == 0:
      quatro += 1
    else:
      double += 1

if double == N:
  print("Yes")
  exit()
plus = 0
if double != 0:
  plus = 1
if plus + odd - 1 <= quatro:
  print("Yes")
else:
  print("No")
