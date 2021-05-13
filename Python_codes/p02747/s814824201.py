s = input().split('hi')
ans = 'Yes'
for i in s:
  if i != '':
    ans = 'No'
    break

print(ans)