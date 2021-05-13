N = int(input())
S = str(input())

ans = S[1:].count('E')
tmp = S[1:].count('E')
for i in range(N-1):
  if S[i] == 'W':
    tmp += 1
  if S[i+1] == 'E':
    tmp -= 1
  ans = min(ans, tmp)
    
print(ans)