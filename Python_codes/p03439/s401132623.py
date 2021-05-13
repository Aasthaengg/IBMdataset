N = int(input())
M = 18
left = 0
right = N-1
print(left)
l = input()
if l != "Vacant":
  print(right)
  r = input()
  if r != "Vacant":
    notOK = True
    while notOK:
      middle = (right+left)//2
      print(middle)
      s = input()
      if s == "Vacant":
        notOK = False
        break
      elif (middle-left)%2 == 0 and l != s:
        right = middle
        r = s
      elif (middle-left)%2 == 1 and l == s:
        right = middle
        r = s
      else:
        left=middle
        l = s
