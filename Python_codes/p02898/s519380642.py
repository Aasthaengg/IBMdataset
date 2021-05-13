N, K = map(int, input().split())
h = list(map(int, input().split()))

total = 0
for height in h:
  if height >= K:
    total += 1
    
print(total)