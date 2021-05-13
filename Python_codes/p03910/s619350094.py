N = int(input())

s = 0
i = 0
ans = []
while s < N:
  i += 1
  s += i
  ans.append(i)
dele = s - N
if dele != 0:
  ans.remove(dele)

for t in ans:
  print(t)