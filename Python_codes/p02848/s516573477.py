N = int(input())
S = str(input())


num2alpha = lambda c: chr(c+64)
#0 ~ 25
alpha2num = lambda c: ord(c) - ord('A')

ans = [0] * len(S)
for i in range(len(S)):
  now = alpha2num(S[i]) + N
  now %= 26
  ans[i] = num2alpha(now + 1)
  
for i in range(len(S)):
  print(ans[i], end = "")