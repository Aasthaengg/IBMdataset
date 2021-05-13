S = input()
s_Count = 0
b_Count = 0
ans = 0

for i in range(len(S)):
  if S[i] == "<":
    s_Count += 1
    if i == len(S)-1:
      max_sb = max(s_Count,b_Count)
      min_sb = min(s_Count,b_Count) - 1
      ans += max_sb * (max_sb+1) / 2 + min_sb * (min_sb+1) / 2
      s_Count = 0
      b_Count = 0
  elif S[i] == ">":
    b_Count += 1
    if i == len(S)-1 or S[i+1] == "<":
      max_sb = max(s_Count,b_Count)
      min_sb = min(s_Count,b_Count) - 1
      ans += max_sb * (max_sb+1) / 2 + min_sb * (min_sb+1) / 2
      s_Count = 0
      b_Count = 0
print(int(ans))