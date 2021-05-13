import math

n = int(input())
a = list(map(int,input().split()))

MAX = 1000005
c = [0]*MAX

for i in range(n):
  c[a[i]] += 1

pair = True

for i in range(2,MAX):
  cnt = 0
  for j in range(i,MAX,i):
    cnt += c[j]
  if cnt > 1:
    pair = False

if pair:
  print('pairwise coprime')
else:
  g = a[0]
  for i in range(1,n):
    g = math.gcd(g,a[i])
    
  if g == 1:
    print('setwise coprime')
  else:
    print('not coprime')
