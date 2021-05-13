s = input()
ans = []
s = list(s)

for i in range(len(s)):
  if((i+1)%2 == 1):
    ans.append(s[i])
    
print(''.join(ans))