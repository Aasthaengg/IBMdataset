N = int(input())
S = str(input())

w = S.count('.')
b = S.count('#')
cnt = N+1
tmp = w
for i in range(N):
  if S[i] == '.':
    tmp -= 1
  else:
    tmp += 1
  cnt = min(cnt, tmp)
    
ans = min(w, b, cnt)
print(ans)