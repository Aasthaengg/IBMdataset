S = input()
N = len(S)
 
def isp(s):
  n = len(s)
  for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
      return False
  return True
 
if isp(S) and isp(S[0:(N - 1) // 2]):
  print("Yes")
else:
  print("No")