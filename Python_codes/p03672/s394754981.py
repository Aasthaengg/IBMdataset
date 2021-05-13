def isEvenStr(s):
  if len(s) % 2 == 1:
    return False
  elif s[0:int(len(s)/2)] == s[int(len(s)/2):]:
    return True
  else:
    return False

s = input()
l = len(s)
i = 0

while not isEvenStr(s) or i == 0:
  s = s[:-1]
  i += 1
  if isEvenStr(s):
    print(l - i)