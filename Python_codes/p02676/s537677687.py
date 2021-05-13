K = int(input())
str = list(input())
 
if len(str) <= K:
  print("".join(str))
else:
  print("".join(str[0:K]) + "...")