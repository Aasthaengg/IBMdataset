n,k = map(int,input().split())
s = list(input())
ans = ''

if s[k-1] == 'A':
  s[k-1] = 'a'
elif s[k-1] == 'B':
  s[k-1] = 'b'
else:
  s[k-1] = 'c'
  
for i in s:
  ans += i
  
print(ans)