S = str(input())
ans = 0
B = 1
for i in range(len(S)-1,-1,-1):
  if S[i] == "B":
    ans += len(S[i:-B])
    B += 1

print(ans)