N = int(input())
S = list(input())

ans,x = 0,0

for i in range(N):
  s = S[i]
  if s == 'I':
    x += 1
  else:
    x -= 1
    
  ans = max(ans,x)
  
print(ans)