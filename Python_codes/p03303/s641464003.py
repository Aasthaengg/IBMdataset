S=input()
w=int(input())

import sys
j=0
result=""
while True:
 try:
  result+=S[j]
  j+=w
 except:
  print(result)
  sys.exit()