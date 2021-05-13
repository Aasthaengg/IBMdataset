S = input()

SR = S[::-1]
ans = 0

for i in range(len(S)//2):
  if S[i] != SR[i]:
    ans +=1
  
print(ans)