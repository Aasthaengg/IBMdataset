n, k, s = map(int, input().split())

if s < 10**9:

  if k > 0: 
      aa = [s]*k + [s+1]*(n-k)
  elif k == 0:
      aa = [s+1]*n

else:
  aa =[s]*k + [1]*(n-k)

print(*aa)