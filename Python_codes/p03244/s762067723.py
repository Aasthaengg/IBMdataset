N = int(input())
As = list(map(int, input().split()))
 
dico = {}
dice = {}
for i in range(N):
  if i % 2 == 0:
    if As[i] not in dice:
      dice[As[i]] = 1
    else:
      dice[As[i]] += 1
  else:
    if As[i] not in dico:
      dico[As[i]] = 1
    else:
      dico[As[i]] += 1
    
cnto = [0,0]
cnte = [0,0]
 
o = -1
e = -1
for k in dico:
  if dico[k] > cnto[0]:
    cnto[1] = cnto[0]
    cnto[0] = dico[k]
    o = k
  elif dico[k] > cnto[1]:
    cnto[1] = dico[k]
    
for k in dice:
  if dice[k] > cnte[0]:
    cnte[1] = cnte[0]
    cnte[0] = dice[k]
    e = k
  elif dice[k] > cnte[1]:
    cnte[1] = dice[k]
  
if o == e:
  print(N-max(cnto[0]+cnte[1],cnte[0]+cnto[1]))
else:  
  print(N-cnto[0]-cnte[0])