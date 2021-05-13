n,k = map(int, input().split())
H = [int(input()) for i in range(n)]
H.sort()
ans = max(H)
for i in range(n-k+1):
  p = H[i+k-1] - H[i]
  ans = min(ans,p)
  if ans == 0:
    print(0)
    exit()
  
print(ans)