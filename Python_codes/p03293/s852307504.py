s = str(input())
t = str(input())
k = False
for i in range(len(s)):
  s = s[-1] + s[:-1]
  if s == t:
    k = True
    break
    
print('Yes' if k else 'No')