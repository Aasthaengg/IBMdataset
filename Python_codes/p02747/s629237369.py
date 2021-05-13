s = input().split('i')

h = s[:len(s)-1]
space = s[len(s)-1]
ans = 'No'

for j in h:
  if j =='h' and space == '':
    ans = 'Yes'
  else:
    ans = 'No'
    break
  
print(ans)
