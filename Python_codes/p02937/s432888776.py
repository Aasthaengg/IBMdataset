import string
s = input()
t = input()
l = []
alp = string.ascii_lowercase
G = dict([(alp[i],-1) for i in range(len(alp))])
for i in range(len(s)-1,-1,-1):
  l.append(G.copy())
  G[s[i]] = i
l = l[::-1]  
stG = G.copy()

cnt = 0
ind = 0
while ind < len(t): 
  if stG[t[ind]] == -1:
    cnt = -1
    break
  else:
    lind = stG[t[ind]]
    ind += 1
    if ind >= len(t):
      cnt += 1
      break 
    while l[lind][t[ind]] != -1:   
      lind = l[lind][t[ind]]
      ind += 1
      if ind >= len(t):
        break          
    cnt += 1

###    
if cnt != -1:      
  print(cnt*len(s)-(len(s)-(lind+1)))
else:
  print(cnt)  