n = int(input())
n_s = {}
for i in range(n):
  s = input()
  if s in n_s:
    n_s[s] += 1
  else:
    n_s[s] = 1

m = int(input())

for i in range(m):
  s = input()
  if s in n_s:
    n_s[s] -= 1
  else:
    n_s[s] = -1

if max(n_s.values()) < 0 :
  print(0)
else:
  print(max(n_s.values()))