l = [[[0 for z in range(10)] for y in range(3)] for x in range(4)]
n = int(input())
while n > 0:
  b,f,r,v = map(int,input().split())
  l[b-1][f-1][r-1] += v
  n -= 1
c = 0
for b in l:
  c += 1
  for f in b:
    r_l = [str(r) for r in f]
    print(' '+' '.join(r_l))
  if c < len(l):  
    print('#'*20)