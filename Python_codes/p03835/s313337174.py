K, S = map(int, input().split())
ans = 0
for X in range(max(0, S-2*K), min(K, S)+1):
  for Y in range(max(0, S-X-K), min(K, S-X)+1):
    ans += 1
    
print(ans)