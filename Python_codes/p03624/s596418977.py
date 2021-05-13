S=input()
l=[0]*26
for i in range(len(S)):
  l[ord(S[i])-97]+=1
for j in range(26):
  if l[j]==0:
    print(chr(j+97))
    break
else:
  print("None")