import sys
readline = sys.stdin.readline

# 両端から見ていき、回文になっていないときに片方がxだったら、ans += 1してxのほうのインデックスを1進める
# 両方ともxでなかったら-1を出力

S = readline().rstrip()

left = 0
right = len(S) - 1
ans = 0
while left < right:
  if S[left] == S[right]:
    left += 1
    right -= 1
  else:
    if S[left] == "x":
      ans += 1
      left += 1
    elif S[right] == "x":
      ans += 1
      right -= 1
    else:
      print(-1)
      break
else:
  print(ans)