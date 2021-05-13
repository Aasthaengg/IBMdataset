n = int(input())
tn = [int(num) for num in input().split()]
m = int(input())

pxn = []
for _ in range(m):
  p, x = map(int, input().split())
  pxn.append([p, x])
  
for p in pxn:
  print(sum(tn) - tn[p[0]-1] + p[1])