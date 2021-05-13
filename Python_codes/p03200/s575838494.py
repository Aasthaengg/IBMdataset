S = list(input())
ans = 0
l = len(S)
for i in range(l-1, -1, -1):
  x = l
  if(S[i]=='B'):
    ans += (x-i-1)
    l -= 1
print(ans)