N = input()

def rest_nine(x):
  for i in range(1, len(x)):
    if int(x[i]) != 9:
      return False
  return True

if rest_nine(N):
  print(int(N[0])+(len(N)-1)*9)
else:
  print(int(N[0])-1+(len(N)-1)*9)