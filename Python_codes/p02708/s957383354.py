modprime = 10**9+7
n, k = map(int, input().split())
big_total = 0
# fix the number of selected
for z in range(k, n+2):
  min_sum = (z-1)*z//2
  max_sum = n*(n+1)//2 - (n-z)*(n-z+1)//2
  # all intermediate sums are possible
  num_sums = max_sum - min_sum + 1
  big_total = (big_total + num_sums)%modprime
print(big_total)