s=list(input())

ans = []

for i in s:
  if i == '?':
    ans.append('D')
  else:
    ans.append(i)

print(''.join(map(str,ans)))