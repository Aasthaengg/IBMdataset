S=input()
T=input()
ans=0
for x in range(3):
  if S[x]==T[x]:
    ans += 1
print(ans)
