S=input()
n=len(S)
ans="Good"
for i in range(1,n):
  if S[i]==S[i-1]:
    ans="Bad"
    break
print(ans)