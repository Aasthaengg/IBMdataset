S = input().strip()

# 左右から詰めていく
l = 0
r = len(S)-1
ans = 0
while l != r and l <= r:
  if S[l] == 'x' and S[r] != 'x':
    l += 1
    ans += 1
  elif S[l] != 'x' and S[r] == 'x':
    r -= 1
    ans += 1
  elif S[l] != S[r]:
    print(-1)
    exit()
  else:
    l += 1
    r -= 1
  
print(ans)