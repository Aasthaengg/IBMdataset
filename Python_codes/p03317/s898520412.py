N,M = map(int,input().split())

ans = (N-1) // (M-1)

if (N-1) % (M-1) != 0:
  ans += 1
  
print(ans)
