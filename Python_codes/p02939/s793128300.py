S = input()
ans = 1
prev = S[0]
i = 1

while i < len(S):
  tmp = S[i]
  while 1:
    if prev != tmp:
      break
    else:
      i += 1
      tmp += S[i]
  
  if i == len(S) - 2 and tmp == S[-1]:
    tmp += S[-1]
    i += 1
  ans += 1
  i += 1
  prev = tmp
print(ans)