import sys
input = sys.stdin.readline
n = int(input())
f = []
for i in range(n):
  f.append(list(map(int, input().split())))
p = []
for i in range(n):
  p.append(list(map(int, input().split())))

cand = []
for i in range(1, 2 ** 10):
  cnt = [0] * n
  for j in range(10):
    if i & (1 << j):
      for k in range(n):
        if f[k][j]:
          cnt[k] += 1
  v = 0
  for k in range(n):
    v += p[k][cnt[k]]
  cand.append(v)
    
print(max(cand))
  
