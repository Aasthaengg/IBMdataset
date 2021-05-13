S = input()
k = []
ans = ""
for i in range(len(S)):
  k.append(S[i])
if len(k) == 2:
  for i in range(2):
    ans += k[i]
else:
  k.reverse()
  for i in range(3):
    ans += k[i]
print(ans)