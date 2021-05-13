S = input()
S = sorted(S)
ans = 'None'
for i in range(97, 123):
    if S.count(chr(i)) > 0:
      continue
    else:
      ans = chr(i)
      break
print(ans)