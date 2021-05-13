D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) for _ in range(D)]
last = [0 for i in range(26)]
sat = 0

for d in range(D):
  sat += s[d][t[d]-1]
  last[t[d]-1] = d+1
  for i in range(26):
    sat -= c[i] * (d+1 - last[i])
  print(sat)