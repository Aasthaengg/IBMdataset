s = input()
ans = 'Yes'
for i,k in enumerate(s):
  num = i + 1
  if num % 2 == 0 and k not in set('LUD'):
    ans = 'No'
    break
  if num % 2 == 1 and k not in set('RUD'):
    ans = 'No'
    break
print(ans)