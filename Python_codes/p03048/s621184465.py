R, G, B, n = map(int, input().split())
cnt = 0
for r in range((n//R)+1):
  for g in range((n//G)+1):
    
      if (n - (r*R + g*G)) % B == 0 and n - (r*R + g*G) >= 0:
        
        cnt +=1
print(cnt)