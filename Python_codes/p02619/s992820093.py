D = int(input())
c = list(map(int, input().split()))
s = []
for d in range(D):
	s.append(list(map(int, input().split())))
last = [0 for i in range(26)]
v = 0
for d in range(1, D+1):
  i = int(input())
  last[i-1] = d
  v += s[d-1][i-1]
  for k in range(26):
    v -= c[k] * (d - last[k])
  print(v)