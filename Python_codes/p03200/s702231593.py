S = input()
ans = 0
x = 0
for i in range(len(S)-1, -1, -1):
  if S[i] == "W":
    x += 1
  else:
    ans += x
print(ans)