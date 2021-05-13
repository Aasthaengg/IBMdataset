S = input()
T = input()
len_S = len(S)
ans = 0
for i in range(0,len_S):
  if(S[i] != T[i]):
    ans += 1
print(ans)