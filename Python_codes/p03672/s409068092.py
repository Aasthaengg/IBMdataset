s = input()
i=1
while True:
  if s[:(len(s)-2*i)//2] == s[(len(s)-2*i)//2:len(s)-2*i]:
    print(len(s)-2*i)
    exit()
  else:
    i += 1