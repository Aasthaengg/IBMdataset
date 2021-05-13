N = int(input())
s = [list(input()) for _ in range(2)]
mod = 10**9+7
ans = 1
i = 0
pre = -1
while i < N:
  if s[0][i] == s[1][i]: # 縦
    if pre == -1:
      ans *= 3
    elif pre == 0:
      ans *= 1
    elif pre == 1:
      ans *= 2

    ans %= mod
    pre = 1
    i += 1
  elif s[0][i] == s[0][i+1]: # 横
    if pre == -1:
      ans *= 6
    elif pre == 0:
      ans *= 3
    elif pre == 1:
      ans *= 2
    
    ans %= mod
    pre = 0
    i += 2
print(ans)