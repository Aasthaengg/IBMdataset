N, K = map(int, input().split())

count = 0
for i in range(K, N + 2): 
  count += (i * (N + N - i + 1) / 2 - i * (i - 1) / 2 + 1) % 1000000007
  
print(int(count % 1000000007))