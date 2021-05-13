S = input()

s_sort = sorted(list(S))

new_character = "?"

if len(S) < 26:
  for  s in range(97,123,1):
    if S.count(chr(s))==0:
      new_character = chr(s)
      print(S + new_character)
      break
else:
  if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
  else:
    for x in range(25,0,-1):
      if ord(S[x-1]) < ord(S[x]):
        letters = sorted([ord(n) for n in list(S[x:])])
        letter = chr([l for l in letters if l >= ord(S[x-1])][0])
        ans = S[:x-1] + letter
        print(ans)
        break
      
