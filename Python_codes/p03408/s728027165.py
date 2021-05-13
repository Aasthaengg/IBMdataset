n = int(input())
s = dict()
for _ in range(n):
  temp = input()
  try:
    s[temp] += 1
  except:
    s[temp] = 1

m = int(input())

for _ in range(m):
  temp = input()
  try:
    s[temp] -= 1
  except:
    s[temp] = 1


s = sorted(s.items(), key=lambda x: x[1], reverse=True)

if s[0][1] < 0:
  print(0)
else:
  print(s[0][1])

