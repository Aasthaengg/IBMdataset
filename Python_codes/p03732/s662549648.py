N,W = map(int,input().split())
L = []
for i in range(N):
  L.append(list(map(int,input().split())))
Vmax = 0
w_1 = []
w_2 = []
w_3 = []
w_4 = []
for i in range(N):
  if L[i][0] == L[0][0]:
    w_1.append(L[i][1])
  elif L[i][0] == L[0][0]+1:
    w_2.append(L[i][1])
  elif L[i][0] == L[0][0]+2:
    w_3.append(L[i][1])
  else:
    w_4.append(L[i][1])
w_1.sort()
w_2.sort()
w_3.sort()
w_4.sort()
w_1.reverse()
w_2.reverse()
w_3.reverse()
w_4.reverse()
for i in range(1,len(w_1)):
  w_1[i] = w_1[i-1]+w_1[i]
for i in range(1,len(w_2)):
  w_2[i] = w_2[i-1]+w_2[i]
for i in range(1,len(w_3)):
  w_3[i] = w_3[i-1]+w_3[i]
for i in range(1,len(w_4)):
  w_4[i] = w_4[i-1]+w_4[i]
w_1.append(0)
w_2.append(0)
w_3.append(0)
w_4.append(0)
for j in range(len(w_1)):
  for k in range(len(w_2)):
    for l in range(len(w_3)):
      for m in range(len(w_4)):
        if j*L[0][0]+k*(L[0][0]+1)+l*(L[0][0]+2)+m*(L[0][0]+3) > W:
          continue
        else:
          if w_1[j-1]+w_2[k-1]+w_3[l-1]+w_4[m-1] >= Vmax:
            Vmax = w_1[j-1]+w_2[k-1]+w_3[l-1]+w_4[m-1]
print(Vmax)