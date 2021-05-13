N, K = [int(n) for n in input().split()]

count = 0
for b in range(1, N + 1):
  p = N // b 
  count += p * max(0, b - K)
  r = N % b
  count += max(r - K + 1, 0)
if K == 0:
  count -= N
print(count)
  

