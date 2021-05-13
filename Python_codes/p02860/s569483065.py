r = int(input())
s = input()

if r%2 == 1:
  print("No")
  exit()
m = str(s[0:r//2])

if m*2 == s:print('Yes')
else:print('No')