dic = [False for i in range(26)]
txt = input()
for i in txt:
  dic[ord(i) - 97] = True
for i in range(26):
  if not dic[i]:
    print(txt + chr(i + 97))
    break
else:
  for j in range(25):
    if txt[24 - j] < txt[25 - j]:
      
      last = txt[24-j] #以降の文字列を修正
      txt = txt[:24 - j]
      
      dic = [False for i in range(26)]
      for k in txt:
        dic[ord(k) - 97] = True
      txt += chr(dic[ord(last) - 96:].index(False) + ord(last) + 1)

      print(txt)
      break

  else:
    print(-1)