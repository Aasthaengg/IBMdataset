S = input()
N = len(S)

ans1 = 0
ans2 = 0

for i in range(N):
  if i%2 == 0:
    if S[i] != "0":
      ans1 += 1
    else:
      ans2 += 1
  else:
    if S[i] != "1":
      ans1 += 1
    else:
      ans2 += 1

print(min(ans1, ans2))