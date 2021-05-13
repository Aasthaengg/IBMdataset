s = input()
ans = 0
for i in range(len(s)):
  for j in range(i+1,len(s)+1):
    t = s[i:j].replace('A','')
    t = t.replace('C','')
    t = t.replace('G','')
    t = t.replace('T','')
    if t == '':
      ans = max(j-i,ans)
print(ans)