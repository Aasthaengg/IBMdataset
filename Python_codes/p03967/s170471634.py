S=input()

ans=0
for i in range(len(S)):
  if i%2==0:
    ans -= 0 if S[i]=="g" else 1
  else:
    ans += 1 if S[i]=="g" else 0
print(ans)