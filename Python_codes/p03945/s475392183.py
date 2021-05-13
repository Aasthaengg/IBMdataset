s = input()

if s[-1] == 'B':
   new = 'W'
else:
   new = 'B'

if s == s[0] * len(s):
   print(0)
   exit()

ans = 0
for i in reversed(range(len(s)-1)):
   if s[i] == new:
      ans += 1
      if new == 'B':
         new = 'W'
      else:
         new = 'B'
print(ans)
