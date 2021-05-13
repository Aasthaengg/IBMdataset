d = int(input())
c = list(map(int, input().split()))
s = [[] for _ in range(d)]
for i in range(d):
  s[i] = list(map(int, input().split()))
  
last = [0 for _ in range(26)]

def loss(today):
  sum = 0
  for i in range(26):
    sum += c[i-1] * (today - last[i-1])
  return sum
  
  
v = 0
for today in range(1, d+1):
  t = int(input())
  last[t-1] = today
  v += s[today-1][t-1]
  v -= loss(today)
  print(v)