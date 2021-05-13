word1,word2,word3 = map(str,input().split())
if word1[-1] == word2[0] and word2[-1] == word3[0]:
  print("YES")
else:
  print("NO")