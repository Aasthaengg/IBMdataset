n, k = map(int, input().split())

if k == 0:
  print(n**2)
  exit()

ans  = 0

for b in range(1,n+1):

  # 連続部分
  if b - k > 0:
    ans += (n // b) * (b-k)
    
  # 繰り返し範囲外
  if ((n - (n // b)*b) - (k-1)) > 0:
    ans += ((n - (n // b)*b) - (k-1))


  
  
print(ans)