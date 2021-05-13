S=input()
w=int(input())
ans=""

for x in range(len(S)):
  if x%w==0:
    ans += S[x]
print(ans)