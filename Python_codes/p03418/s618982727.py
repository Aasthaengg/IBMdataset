def count_possible_pairs(N, K):
  if K == 0:
    return N**2
  else:
    cnt = 0      
    for b in range(K+1, N+1):
      block = (N+1) // b
      cnt += block * (b - K)    # remainders are K, K+1, ..., b-1
      res = (N+1) % b
      if res > K:
        cnt += (res - K)
    return cnt




N, K = map(int, input().split())
print(count_possible_pairs(N, K))
