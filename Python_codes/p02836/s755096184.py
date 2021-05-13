S = input()
ans = 0

for n in range(len(S)//2):
  if S[n] != S[-n-1]:
    ans+=1
    
print(ans)