N = int(input())
l = []

for i in range(N):
  s,p = input().split()
  l.append([i+1,[s,-int(p)]])
  
sl = sorted(l,key=lambda w: w[1])
for w in sl:
  print(w[0])