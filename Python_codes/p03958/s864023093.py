K, T = map(int, input().split())
cakes = list(map(int, input().split()))
max_c = 0
sum_c = 0
for cake in cakes:
  max_c = max(max_c, cake)
  sum_c += cake
print(max(0, 2*max_c-sum_c-1))