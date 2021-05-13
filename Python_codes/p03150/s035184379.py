S = str(input())

str_keyence = "keyence"

if S.find("keyence")==0 or S.rfind("keyence")==len(S)-7:
  print("YES")
else:
  for i in range(1,7):
      #print(str_keyence[0:i],str_keyence[i:])
      #print(S.find(str_keyence[0:i]))
      #print(S.find(str_keyence[i:]))
      if S.find(str_keyence[0:i])==0 and S.rfind(str_keyence[i:])==len(S)-len(str_keyence[i:]):
          print("YES")
          break
  else:
      print("NO")