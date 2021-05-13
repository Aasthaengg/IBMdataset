N, K = map(int, input().split())
P = tuple(map(int, input().split()))
P2 = P[K:]

max_sum = 0
sum_ = sum(P[:K])

for p, q in zip(P, P2):
  max_sum = max(max_sum, sum_)
  sum_ += q - p
  
max_sum = max(max_sum, sum_)
          
res = (max_sum + K)/ 2
print(res)