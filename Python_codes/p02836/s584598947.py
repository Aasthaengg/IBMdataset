s = input()
n = len(s)
ans = 0
for i in range(0,n//2):
  if s[i] != s[(-1)*(i+1)]:
    ans += 1
 
print(ans)