N=int(input())
S=input()
ans=0
for x in range(N-2):
  if S[x]=='A':
    if S[x+1]=='B':
      if S[x+2]=='C':
        ans += 1
print(ans)