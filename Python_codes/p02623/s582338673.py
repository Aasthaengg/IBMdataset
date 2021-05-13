n, m, k = map(int, input().split(' '))
a_list = list(map(int, input().split(' ')))
b_list = list(map(int, input().split(' ')))
sa = [0] * (n+1)
sb = [0] * (m+1)

for i in range(n):
  sa[i+1] = a_list[i] + sa[i]
for j in range(m):
  sb[j+1] = b_list[j] + sb[j]

best=0
r = m
for i, a in enumerate(sa):
  if a>k:
    break
  while ((a + sb[r]) > k) & (r>=0):
    r-=1
    
  best = max(best,i+r)
      
  
    
print(best)