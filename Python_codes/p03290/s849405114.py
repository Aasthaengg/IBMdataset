D, G = map(int, input().split())
qu = [0] * D
bonus = [0] * D
for i in range(D):
  a, b = map(int, input().split()) 
  qu[i] = a
  bonus[i] = b
  
ans = 10 ** 5  
for i in range(2 ** D):
  score = 0
  nn = 0
  yet = [0] * D
  for j in range(D):#j の 問い をコンプリートする
    if (i >> j) & 1:
      score += 100 * (j + 1) * qu[j] + bonus[j]
      nn += qu[j]
      yet[j] = 1
  if score >= G:
    ans = min(ans, nn)
  else:
    #print(i, score, nn)
    con = 0
    for k in range(1, D + 1):
      if con == 0:
        if yet[D - k] == 0:
          now = 100 * (D - k + 1) * (qu[D - k] - 1)
          if now + score >= G:
            subt = G - score
            nn += int((subt - 1) / (100 * (D - k + 1))) + 1
            ans = min(ans, nn) 
            con = 1
          else:
            score += now
            nn += qu[D - k] - 1
  #print(ans)    
print(ans)    
    
    
  
  
  
