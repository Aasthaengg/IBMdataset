S = list(input())
ans = int("".join([S[0],S[1],S[2]]))
for i in range(len(S)-2):
  n = int("".join([S[i],S[i+1],S[i+2]]))
  if abs(n-753) <= abs(ans-753):
    ans = n
  else:
    pass
  
print(abs(753-ans))