n,k = map(int,input().split())
s = input()
k -= 1
ans = ''
for i in range(n):
    if i == k:
      if s[k] == 'A': ans += 'a'
      elif s[k] == 'B': ans += 'b'
      else: ans += 'c'
    else: ans += s[i]
print(ans)