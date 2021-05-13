abcde = [int(input()) for _ in range(5)]

s = 0
t = 125
for i in range(5):
  if abcde[i]%10 != 0:
    if int(str(abcde[i])[-1]) < t:
      s = i
      t = int(str(abcde[i])[-1])

ans = 0
for i in range(5):
  if s == i: continue
  if abcde[i] % 10 == 0: ans += abcde[i]
  else:
    while abcde[i]%10 != 0:
      abcde[i] += 1
    ans += abcde[i]
print(ans+abcde[s])