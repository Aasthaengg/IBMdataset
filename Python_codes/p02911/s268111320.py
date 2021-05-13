n,k,q = map(int, input().split())


point_l = [k-q] * n
for _ in range(q):
 ans = int(input())
 point_l[ans-1] += 1

for i in range(n):
  print('Yes' if point_l[i]>0 else 'No')