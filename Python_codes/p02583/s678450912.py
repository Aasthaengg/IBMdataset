n = int(input())
l = [int(i) for i in input().split()]
cnt = 0
for i in range(n-2):
  l1 = l[i]
  for j in range(i+1, n-1):
    l2 = l[j]
    for g in range(j+1, n):
      l3 = l[g]
      l1_, l2_, l3_ = sorted([l1, l2, l3])
      if l1_ == l2_ or l2_ == l3_:
        continue
      if l3_ < l2_ + l1_:
        cnt += 1
        #print(i+1, j+1, g+1, l3_, l2_, l1_)
print(cnt)