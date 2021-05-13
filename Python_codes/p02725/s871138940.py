k,n = map(int, input().split())
a = [int(x.strip()) for x in input().split()]
min_dist = k
for i in range(n):
  if i != 0 and i != n-1:
    dist_r = a[i-1] + (k - a[i])
    dist_l = a[i] + (k - a[i+1])
    if min_dist > min(dist_r,dist_l):
      min_dist = min(dist_r,dist_l)
  elif i == 0:
    dist_r = a[n-1] - a[i]
    dist_l = a[i] + (k - a[i+1])
    min_dist0 = min(dist_r,dist_l)
  else:
    dist_r = a[i-1] + (k - a[i])
    dist_l = a[i] - a[0]
    min_distn = min(dist_r,dist_l)
ans = min(min_dist,min_dist0,min_distn)
print(ans) 