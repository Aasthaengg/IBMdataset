
def isPalindrome(str):
  ret = True
  l = len(str)
  end = int(l/2)
  for i in range(end):
    if str[i] != str[-1-i]:
      ret = False
	
  return ret

ans = "Yes"
str = input()

str_l = len(str)
if isPalindrome(str) and isPalindrome(str[:int(str_l/2)]) and isPalindrome(str[-int(str_l/2):]):
  print("Yes")
else:
  print("No")