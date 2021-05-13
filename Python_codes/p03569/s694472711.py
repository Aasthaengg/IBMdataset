S = input()
l = 0
r = len(S) - 1
ans = 0
while l < r:
  if S[l] == S[r]:
    l += 1
    r -= 1
  elif S[l] == "x":
    l += 1
    ans += 1
  elif S[r] == "x":
    r -= 1
    ans += 1
  else:
    print(-1)
    break
else:
  print(ans)