S = input()
while(len(S) >= 5):
  if(S[-5:] == "dream" or S[-5:] == "erase"):
    S = S[:-5]
  elif(S[-6:] == "eraser"):
    S = S[:-6]
  elif(S[-7:] == "dreamer"):
    S = S[:-7]
  else:
    break
if(len(S) == 0):
  print("YES")
else:
  print("NO")