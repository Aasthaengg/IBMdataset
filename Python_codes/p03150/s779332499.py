S = input()
s = "keyence"
ans = "NO"
 
for i in range(len(S)):
  if s == S[:i] + S[len(S)-len(s)+i:]:
    ans = "YES"
    
print(ans)
