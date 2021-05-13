A, B, C, K = map(int, input().split())

if A >= K:
  print(K)
  exit()
  
temp = K - A

if B >= temp:
  print(A)
  exit()
  
temp = temp - B

print(A - temp)
  
