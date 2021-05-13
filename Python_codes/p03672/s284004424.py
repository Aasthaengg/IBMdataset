s = input()

for i in range(len(s)-1, -1, -1):
  if i%2 == 0:
    m = i//2
    if s[:m] == s[m:i]:
      print(i)
      exit()