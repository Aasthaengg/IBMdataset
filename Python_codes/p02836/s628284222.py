s=list(input())
sr=s[::-1]
ans=0
for i in range(len(s)):
  if s[i]!=sr[i]:
    ans+=1
print(ans//2)